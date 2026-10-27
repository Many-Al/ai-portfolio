# 🤖 دردشة Gemini — تطبيق ويب تفاعلي

تطبيق دردشة ويب مبني بـ **Streamlit** و **Google Gemini API**، مع ذاكرة محادثة من جهة الخادم (Interactions API).

## ✨ الميزات

- 💬 محادثة تفاعلية مع نموذج Gemini
- 🧠 ذاكرة محادثة (يتذكر السياق السابق)
- 🎨 واجهة نظيفة وسريعة (Streamlit)
- ⚙️ شريط جانبي لإدارة المحادثة
- 🛡️ معالجة أخطاء دقيقة (تجاوز الحد، مفتاح خاطئ، نموذج غير متاح)
- 🔐 المفتاح السري محمي في `.env` (غير مرفوع إلى Git)

## 🛠️ التقنيات المستخدمة

| التقنية | الإصدار | الوظيفة |
| :--- | :--- | :--- |
| Python | 3.12 | لغة البرمجة |
| Streamlit | 1.66 | واجهة الويب |
| google-genai | 2.33 | الاتصال بـ Gemini |
| python-dotenv | 1.2 | قراءة المفتاح من `.env` |

## 🚀 التشغيل المحلي

### 1. استنساخ المستودع

```bash
git clone <your-repo-url>
cd gemini-chat-web

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
GEMINI_API_KEY=your_api_key_here
احصل على مفتاحك من: https://aistudio.google.com/apikey

streamlit run app.py 
افتح المتصفح على: http://localhost:8501
gemini-chat-web/
├── app.py               # الكود الرئيسي
├── requirements.txt     # المكتبات المطلوبة
├── .env                 # المفتاح السري (غير مرفوع)
├── .gitignore           # الملفات المستثناة من Git
└── README.md            # هذا الملف



gemini-chat-web/
├── app.py               # الكود الرئيسي
├── requirements.txt     # المكتبات المطلوبة
├── .env                 # المفتاح السري (غير مرفوع)
├── .gitignore           # الملفات المستثناة من Git
└── README.md            # هذا الملف
🔒 الأمان
المفتاح السري في .env فقط.

.env مضاف إلى .gitignore — لا يُرفع إلى Git أبداً.

الأخطاء تُسجَّل من جهة الخادم ولا تُعرض للمستخدم.

📝 ملاحظات
الذاكرة من جهة الخادم عبر previous_interaction_id.

مسح المحادثة من الشريط الجانبي يمسح السجل والذاكرة معاً.

النموذج المستخدم: gemini-3.5-flash-lite (خفيف وسريع).

📄 الترخيص
MIT


---

### بعد اللصق، احفظ:
- `Ctrl + O`
- `Enter`
- `Ctrl + X`

### ثم تحقق:

```bash
head -15 README.md
