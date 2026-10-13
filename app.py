import os
from dotenv import load_dotenv
from google import genai

# تحميل المتغيرات من ملف .env
load_dotenv()

# قراءة المفتاح من ملف .env
api_key = os.getenv("GEMINI_API_KEY")

# إنشاء عميل Gemini
client = genai.Client(api_key=api_key)

# إرسال سؤال لـ Gemini
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="مرحباً، أنا محمود. قل لي جملة ترحيبية قصيرة."
)

# طباعة الرد
print(response.text)
