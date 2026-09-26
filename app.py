# -*- coding: utf-8 -*-
"""خدمة API عامة لأي نموذج - تعمل محلياً وعلى Render وHugging Face"""
from flask import Flask, request, jsonify
import yaml
import joblib
import os
from model_factory import get_model

app = Flask(__name__)

# تحميل الإعدادات
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

print(f"⏳ تحميل النموذج: {config['model_name']} ({config['task_type']})...")

model = None
try:
    if config["task_type"] in ["tabular_classification", "tabular_regression"]:
        model_path = config.get("model_path", "models/model.pkl")
        
        if os.path.exists(model_path):
            model = joblib.load(model_path)
            print("✅ تم تحميل النموذج المدرب من الملف")
        else:
            # تدريب تلقائي إذا لم يوجد الملف (ضروري للنشر على Render)
            print("⚠️ النموذج غير موجود، جاري التدريب التلقائي...")
            from sklearn.datasets import load_iris
            data = load_iris()
            model = get_model(
                config["task_type"],
                config["model_name"],
                config.get("model_params", {})
            )
            model.fit(data.data, data.target)
            os.makedirs(os.path.dirname(model_path), exist_ok=True)
            joblib.dump(model, model_path)
            print(f"✅ تم التدريب والحفظ تلقائياً في: {model_path}")
    else:
        model = get_model(
            config["task_type"],
            config["model_name"],
            config.get("model_params", {})
        )
        print("✅ النموذج جاهز")
except Exception as e:
    print(f"❌ فشل تحميل النموذج: {e}")
    print("   الخدمة ستعمل لكن /predict سيفشل حتى تثبت المكتبات.")


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok" if model else "model_unavailable",
        "task_type": config["task_type"],
        "model_name": config["model_name"]
    })


@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "النموذج غير محمّل"}), 503
    
    data = request.json
    t = config["task_type"]

    if t in ["tabular_classification", "tabular_regression"]:
        pred = model.predict([data["features"]]).tolist()
        return jsonify({"prediction": pred})

    elif t == "anomaly_detection":
        pred = model.predict([data["features"]]).tolist()
        return jsonify({"anomaly": pred})

    elif t == "object_detection":
        results = model(data["image_path"])
        dets = []
        for r in results:
            for b in r.boxes:
                dets.append({
                    "class": model.names[int(b.cls[0])],
                    "confidence": float(b.conf[0])
                })
        return jsonify({"detections": dets})

    elif t == "text_generation":
        return jsonify({"text": model.generate_content(data["prompt"]).text})

    elif t in ["text_classification", "sentiment_analysis"]:
        return jsonify({"result": model(data["text"])})

    elif t == "summarization":
        return jsonify({"summary": model(data["text"], max_length=130)[0]["summary_text"]})

    elif t == "translation":
        return jsonify({"translation": model(data["text"])[0]["translation_text"]})

    elif t == "question_answering":
        return jsonify({"answer": model(question=data["question"], context=data["context"])})

    elif t == "embeddings":
        return jsonify({"embedding": model.encode(data["text"]).tolist()})

    elif t == "speech_to_text":
        return jsonify({"text": model.transcribe(data["audio_path"])["text"]})

    return jsonify({"error": "نوع غير مدعوم في هذه النقطة"}), 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)