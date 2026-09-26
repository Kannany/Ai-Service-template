# -*- coding: utf-8 -*-
"""عميل اختبار - يرسل طلباً للخدمة"""
import requests, json

URL = "http://127.0.0.1:5000/predict"

payload = {"features": [5.1, 3.5, 1.4, 0.2]}  # مثال Iris

r = requests.post(URL, json=payload, timeout=10)
print("الحالة:", r.status_code)
print("الرد:", json.dumps(r.json(), ensure_ascii=False, indent=2))
