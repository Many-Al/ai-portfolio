import os
from dotenv import load_dotenv
from google import genai

# 1. تحميل المتغيرات من ملف .env
load_dotenv()

# 2. قراءة مفتاح API من الذاكرة
api_key = os.getenv("GEMINI_API_KEY")

# 3. إنشاء عميل الاتصال
client = genai.Client(api_key=api_key)

# 4. طلب قائمة النماذج المتاحة من الخادم
print("جاري جلب قائمة النماذج المتاحة...\n")
for model in client.models.list():
    # طباعة اسم النموذج فقط (يتجاهل التفاصيل الأخرى لتسهيل القراءة)
    print(model.name)
