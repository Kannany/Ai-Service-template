# 📊 جدول النماذج حسب المهمة

| نوع المهمة (task_type) | النموذج الموصى به (model_name) | المكتبة | حالة الاستخدام |
|:---|:---|:---|:---|
| `tabular_classification` | `RandomForest` / `XGBoost` | scikit-learn / xgboost | تصنيف بيانات جدولية |
| `tabular_regression` | `RandomForestRegressor` | scikit-learn | توقع أرقام |
| `gradient_boosting` | `XGBoost` | xgboost | تصنيف/انحدار قوي |
| `anomaly_detection` | `IsolationForest` | scikit-learn | كشف الشذوذ |
| `clustering` | `KMeans` | scikit-learn | تجميع البيانات |
| `object_detection` | `yolov8n.pt` / `yolov11n.pt` | ultralytics | كشف الأشياء في الصور |
| `image_classification` | `google/vit-base-patch16-224` | transformers | تصنيف الصور |
| `text_classification` | `aubmindlab/bert-base-arabertv02` | transformers | تصنيف نصوص عربية |
| `sentiment_analysis` | `CAMeL-Lab/bert-base-arabic-camelbert` | transformers | تحليل المشاعر |
| `text_generation` | `gemini-2.5-flash` / `gpt-4o-mini` | google-generativeai / openai | دردشة وتوليد نصوص |
| `summarization` | `facebook/bart-large-cnn` / `gemini` | transformers | تلخيص النصوص |
| `translation` | `Helsinki-NLP/opus-mt-ar-en` | transformers | ترجمة |
| `question_answering` | `deepset/roberta-base-squad2` | transformers | أسئلة وأجوبة |
| `embeddings` | `nomic-embed-text` / `BAAI/bge-m3` | sentence-transformers | أنظمة RAG |
| `speech_to_text` | `base` / `small` / `medium` | openai-whisper | تفريغ صوتي |
| `text_to_speech` | `MeloTTS` / `VibeVoice` | melotts / vibevoice | توليد صوت |
| `time_series_forecast` | `Prophet` / `ARIMA` | prophet / statsmodels | التنبؤ الزمني |

## 🖥️ التوافق مع المنصات

| المنصة | النماذج الخفيفة (sklearn) | النماذج الثقيلة (YOLO/Whisper/Transformers) |
|:---|:---:|:---:|
| **Pydroid3** | ✅ يعمل | ❌ لا يعمل |
| **Google Colab** | ✅ يعمل | ✅ يعمل (مع GPU) |
| **حاسوب/خادم** | ✅ يعمل | ✅ يعمل |
