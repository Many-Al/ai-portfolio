# AI Portfolio - مشاريع الذكاء الاصطناعي

مرحباً! هذا المستودع يحتوي على مجموعة من المشاريع العملية التي تم تطويرها باستخدام Google Gemini API و Python، بهدف عرض المهارات في بناء تطبيقات الذكاء الاصطناعي بشكل احترافي وآمن.

## 📁 المشاريع

### 1. الاتصال الآمن بـ Gemini API (`app.py`)
- **الوصف**: تطبيق أساسي يوضح كيفية الاتصال بنموذج Gemini بشكل آمن.
- **الميزات**: حماية مفاتيح API باستخدام `.env`، وبيئة عمل معزولة (`venv`).
- **كيفية التشغيل**:
  ```bash
  cd ai-portfolio
  source .venv/bin/activate
  python app.py


2. شات بوت يحفظ ذاكرة المحادثة (02-chatbot-history/chatbot.py)
الوصف: تطبيق دردشة تفاعلي يتذكر سياق المحادثة السابقة.
الميزات: استخدام client.chats.create لإدارة الذاكرة تلقائياً، مع معالجة قوية للأخطاء (try/except) لضمان استقرار التطبيق.
كيفية التشغيل:

  cd 02-chatbot-history
  source ../.venv/bin/activate
  python chatbot.py


3. ملخص النصوص الذكي (03-text-summarizer/summarizer.py)
الوصف: أداة تقرأ ملفاً نصياً محلياً طويلاً وتقوم بتلخيصه تلقائياً إلى نقاط رئيسية.
الميزات: التعامل مع الملفات (File I/O)، وهندسة الأوامر (Prompt Engineering) للحصول على مخرجات منظمة.
كيفية التشغيل:

  cd 03-text-summarizer
  source ../.venv/bin/activate
  python summarizer.py

🛠️ متطلبات التشغيل العامة
Python 3.8+
تثبيت المكتبات: pip install -r requirements.txt
ملف .env يحتوي على GEMINI_API_KEY.
👨‍💻 المطور
Mahmoud Alame
مطور تطبيقات ذكاء اصطناعي شغوف ببناء حلول عملية وآمنة.
📄 الرخصة
MIT License


