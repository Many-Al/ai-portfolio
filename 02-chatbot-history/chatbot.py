import os
from dotenv import load_dotenv
from google import genai
from google.genai import errors

# 1. تحميل المتغيرات من ملف .env
load_dotenv()

# 2. إنشاء عميل الاتصال
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 3. إنشاء جلسة دردشة باستخدام موديل أقل ضغطاً
chat = client.chats.create(

model="gemini-3.5-flash-lite",
    config={
        "system_instruction": "أنت مساعد ذكي ومفيد. رد باختصار شديد."
    }
)

print("🤖 البوت جاهز! (اكتب 'خروج' للإنهاء)")

# 4. حلقة التكرار (Loop) لاستمرار الدردشة
while True:
    # أ. أخذ إدخال من المستخدم
    user_input = input("\nأنت: ")
    
    # ب. شرط الخروج من الحلقة
    if user_input.lower() in ['خروج', 'exit', 'quit']:
        print("🤖 مع السلامة!")
        break
    
    # ج. إرسال الرسالة مع حماية من الأخطاء
    try:
        response = chat.send_message(user_input)
        print(f"🤖 البوت: {response.text}")
    except errors.ServerError as e:
        print(f"⚠️ السيرفر مشغول حالياً (خطأ 503)، حاول مرة أخرى بعد قليل.")
    except errors.ClientError as e:
        print(f"️ خطأ في الطلب: {e}")
    except Exception as e:
        print(f"️ حدث خطأ غير متوقع: {e}")
