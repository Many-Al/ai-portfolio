import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors

# 1. تحميل المتغيرات من ملف .env
load_dotenv()

# 2. إنشاء عميل الاتصال
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 3. قراءة محتوى الملف النصي
file_path = "article.txt"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        text_content = file.read()
except FileNotFoundError:
    print(f"❌ خطأ: لم يتم العثور على الملف '{file_path}'. تأكد من وجوده في نفس المجلد.")
    exit(1)

print("📄 تم قراءة الملف بنجاح. جاري طلب التلخيص من الذكاء الاصطناعي...\n")

# 4. بناء الطلب (Prompt) الاحترافي
prompt = f"""
قم بتلخيص النص التالي إلى 3 نقاط رئيسية واضحة ومختصرة باللغة العربية:

النص:
{text_content}
"""

# 5. إرسال الطلب ومعالجة الرد
try:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )
    print("✅ إليك الملخص:")
    print("-" * 40)
    print(response.text)
    print("-" * 40)
    
except errors.ServerError as e:
    print(f"⚠️ السيرفر مشغول حالياً، حاول مرة أخرى بعد قليل.")
except errors.ClientError as e:
    print(f"❌ خطأ في الطلب: {e}")
except Exception as e:
    print(f"❌ حدث خطأ غير متوقع: {e}")
