# 🤖 قالب خدمة الذكاء الاصطناعي

قالب موحد لتحويل أي نموذج ذكاء اصطناعي إلى خدمة API.

## 🚀 التشغيل المحلي
1. ثبّت المكتبات: `pip install -r requirements.txt`
2. درّب النموذج: `python train.py` (أو اترك `app.py` يدربه تلقائياً)
3. شغّل الخدمة: `python app.py`
4. اختبر: `python test_client.py`

## 🧠 تبديل النموذج
عدّل `config.yaml` فقط، ولا تلمس `app.py` أو `model_factory.py`.

## 📦 النشر على Render
- اربط هذا المستودع بـ Render
- اختر "Web Service"
- Render سيستخدم `Dockerfile` تلقائياً

## 📋 المهام المدعومة
راجع `MODELS_TABLE.md` للقائمة الكاملة.
