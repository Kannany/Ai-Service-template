# -*- coding: utf-8 -*-
"""كتالوج النماذج - مرجع برمجي"""

CATALOG = {
    "tabular_classification": {"default": "RandomForest", "lib": "sklearn"},
    "tabular_regression":     {"default": "RandomForestRegressor", "lib": "sklearn"},
    "gradient_boosting":      {"default": "XGBoost", "lib": "xgboost"},
    "anomaly_detection":      {"default": "IsolationForest", "lib": "sklearn"},
    "clustering":             {"default": "KMeans", "lib": "sklearn"},
    "object_detection":       {"default": "yolov8n.pt", "lib": "ultralytics"},
    "image_classification":   {"default": "google/vit-base-patch16-224", "lib": "transformers"},
    "text_classification":    {"default": "aubmindlab/bert-base-arabertv02", "lib": "transformers"},
    "sentiment_analysis":     {"default": "CAMeL-Lab/bert-base-arabic-camelbert", "lib": "transformers"},
    "text_generation":        {"default": "gemini-2.5-flash", "lib": "google-generativeai"},
    "summarization":          {"default": "facebook/bart-large-cnn", "lib": "transformers"},
    "translation":            {"default": "Helsinki-NLP/opus-mt-ar-en", "lib": "transformers"},
    "question_answering":     {"default": "deepset/roberta-base-squad2", "lib": "transformers"},
    "embeddings":             {"default": "nomic-embed-text", "lib": "sentence-transformers"},
    "speech_to_text":         {"default": "base", "lib": "openai-whisper"},
    "text_to_speech":         {"default": "MeloTTS", "lib": "melotts"},
    "time_series_forecast":   {"default": "Prophet", "lib": "prophet"},
}

def get_default(task_type):
    return CATALOG.get(task_type, {}).get("default")

if __name__ == "__main__":
    print(f"📋 عدد المهام المدعومة: {len(CATALOG)}")
    for k, v in CATALOG.items():
        print(f"  {k:25s} → {v['default']}")
