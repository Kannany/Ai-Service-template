# -*- coding: utf-8 -*-
"""مصنع النماذج - لا تعدله، فقط غيّر config.yaml"""

def get_model(task_type, model_name, params=None):
    params = params or {}
    try:
        if task_type == "tabular_classification":
            from sklearn.ensemble import RandomForestClassifier
            return RandomForestClassifier(**params)

        elif task_type == "tabular_regression":
            from sklearn.ensemble import RandomForestRegressor
            return RandomForestRegressor(**params)

        elif task_type == "gradient_boosting":
            import xgboost as xgb
            return xgb.XGBClassifier(**params)

        elif task_type == "anomaly_detection":
            from sklearn.ensemble import IsolationForest
            return IsolationForest(**params)

        elif task_type == "clustering":
            from sklearn.cluster import KMeans
            return KMeans(**params)

        elif task_type == "object_detection":
            from ultralytics import YOLO
            return YOLO(model_name)

        elif task_type == "image_classification":
            from transformers import pipeline
            return pipeline("image-classification", model=model_name)

        elif task_type == "text_classification":
            from transformers import pipeline
            return pipeline("text-classification", model=model_name)

        elif task_type == "sentiment_analysis":
            from transformers import pipeline
            return pipeline("sentiment-analysis", model=model_name)

        elif task_type == "text_generation":
            import google.generativeai as genai
            import os
            genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
            return genai.GenerativeModel(model_name)

        elif task_type == "summarization":
            from transformers import pipeline
            return pipeline("summarization", model=model_name)

        elif task_type == "translation":
            from transformers import pipeline
            return pipeline("translation", model=model_name)

        elif task_type == "question_answering":
            from transformers import pipeline
            return pipeline("question-answering", model=model_name)

        elif task_type == "embeddings":
            from sentence_transformers import SentenceTransformer
            return SentenceTransformer(model_name)

        elif task_type == "speech_to_text":
            import whisper
            return whisper.load_model(model_name)

        elif task_type == "time_series_forecast":
            from prophet import Prophet
            return Prophet(**params)

        else:
            raise ValueError(f"نوع المهمة غير مدعوم: {task_type}")

    except ImportError as e:
        print(f"⚠️ المكتبة المطلوبة غير مثبتة على هذه المنصة: {e}")
        print(f"   ثبّتها بالأمر: pip install <اسم_المكتبة>")
        raise
