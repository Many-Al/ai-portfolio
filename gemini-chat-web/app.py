import os
import logging
from dotenv import load_dotenv
from google import genai
from google.genai import errors
import streamlit as st

# ============================================================
# 1. التسجيل
# ============================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)

# ============================================================
# 2. إعدادات الصفحة
# ============================================================
st.set_page_config(
    page_title="دردشة Gemini",
    page_icon="🤖",
    layout="centered",
)

# ============================================================
# 3. تحميل المفتاح
# ============================================================
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ لم يتم العثور على GEMINI_API_KEY في ملف .env")
    st.stop()

# ============================================================
# 4. الثوابت
# ============================================================
MODEL_NAME = "gemini-3.5-flash-lite"  # نموذج خفيف وسريع — متاح في حسابك
MAX_OUTPUT_TOKENS = 2048
MAX_INPUT_CHARS = 2000

# ============================================================
# 5. العميل
# ============================================================
@st.cache_resource
def get_client():
    return genai.Client(api_key=API_KEY)

client = get_client()

# ============================================================
# 6. حالة الجلسة
# ============================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_interaction_id" not in st.session_state:
    st.session_state.last_interaction_id = None

# ============================================================
# 7. الشريط الجانبي
# ============================================================
with st.sidebar:
    st.header("⚙️ الإعدادات")
    st.write(f"**النموذج:** `{MODEL_NAME}`")
    st.write(f"**عدد الرسائل:** {len(st.session_state.messages)}")

    if st.button("🗑️ مسح المحادثة", use_container_width=True):
        st.session_state.messages = []
        st.session_state.last_interaction_id = None
        logger.info("تم مسح المحادثة")
        st.rerun()

    st.divider()
    st.caption("مدعوم بـ Interactions API")

# ============================================================
# 8. الواجهة الرئيسية
# ============================================================
st.title("🤖 دردشة Gemini")
st.caption("محادثة تفاعلية مع ذاكرة")

# عرض الرسائل السابقة
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ============================================================
# 9. حقل الإدخال + المعالجة
# ============================================================
if prompt := st.chat_input("اكتب سؤالك هنا...", max_chars=MAX_INPUT_CHARS):
    prompt = prompt.strip()

    if not prompt:
        st.warning("⚠️ الرسالة فارغة.")
        st.stop()

    # عرض وحفظ رسالة المستخدم
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # استدعاء Gemini
    with st.chat_message("assistant"):
        with st.spinner("⏳ جاري التفكير..."):
            try:
                interaction = client.interactions.create(
                    model=MODEL_NAME,
                    input=prompt,
                    previous_interaction_id=st.session_state.last_interaction_id,
                    generation_config={
                        "max_output_tokens": MAX_OUTPUT_TOKENS,
                    },
                )

                reply = getattr(interaction, "output_text", None) or ""

                if not reply.strip():
                    reply = "⚠️ لم يتم إرجاع أي نص من النموذج."

                st.markdown(reply)

                # حفظ الرد + تحديث الـ ID
                st.session_state.messages.append(
                    {"role": "assistant", "content": reply}
                )
                st.session_state.last_interaction_id = interaction.id

            except errors.ClientError as e:
                code = getattr(e, "code", None)
                if code == 429:
                    st.warning("⏳ تجاوزت حد الاستخدام. حاول بعد قليل.")
                    logger.warning(f"Rate limit: {e}")
                    # لا تحذف رسالة المستخدم — قد يعيد المحاولة
                elif code in (401, 403):
                    st.error("🔒 مفتاح API غير صالح. تحقق من ملف .env.")
                    logger.exception(f"Auth error: {e}")
                    st.session_state.messages.pop()
                elif code == 404:
                    st.error(f"❌ النموذج `{MODEL_NAME}` غير موجود أو غير متاح.")
                    logger.exception(f"Model not found: {e}")
                    st.session_state.messages.pop()
                else:
                    st.error("❌ خطأ في الطلب. تحقق من صحة المدخلات.")
                    logger.exception(f"ClientError: {e}")
                    st.session_state.messages.pop()

            except errors.ServerError as e:
                st.error("⚠️ الخوادم مشغولة حالياً. حاول بعد قليل.")
                logger.exception(f"ServerError: {e}")
                st.session_state.messages.pop()

            except Exception as e:
                st.error("❌ حدث خطأ غير متوقع.")
                logger.exception(f"Unexpected error: {e}")
                st.session_state.messages.pop()










