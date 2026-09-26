import os

# الانتقال إلى مجلد القالب
os.chdir("ai_service_template")

# التأكد من وجود مجلد models
os.makedirs("models", exist_ok=True)

# إنشاء ملف .gitkeep فارغ
with open("models/.gitkeep", "w") as f:
    pass  # ملف فارغ تماماً

# التحقق
if os.path.exists("models/.gitkeep"):
    size = os.path.getsize("models/.gitkeep")
    print(f"✅ تم إنشاء models/.gitkeep (الحجم: {size} بايت)")
else:
    print("❌ فشل الإنشاء")

# عرض محتويات مجلد models
print("\n📂 محتويات مجلد models:")
for item in os.listdir("models"):
    print(f"   - {item}")