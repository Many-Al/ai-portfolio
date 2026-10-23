import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# تحميل المتغيرات البيئية
load_dotenv()

# إعداد الصفحة
st.set_page_config(page_title="مساعد محمود الذكي", page_icon="🤖")

st.title("🤖 مساعد محمود الذكي")
st.write("تطبيق دردشة تفاعلي مدعوم بـ Google Gemini API")

# تهيئة العميل مرة واحدة فقط وتجنب إغلاقه
@st.cache_resource
def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    return genai.Client(api_key=api_key)

client = get_client()

# الاحتفاظ بجلسة الدردشة في ذاكرة ستريمليت للـ Session
if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(
        model="gemini-3.5-flash-lite",
        config={
            "system_instruction": "أنت مساعد ذكي ومفيد. رد باختصار شديد."
        }
    )

# تخزين الرسائل لعرضها في الواجهة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# إدخال المستخدم
if user_input := st.chat_input("اكتب رسالتك هنا..."):
    # عرض رسالة المستخدم
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # توليد الرد من البوت
    with st.chat_message("assistant"):
        try:
            response = st.session_state.chat.send_message(user_input)
            bot_reply = response.text
            st.markdown(bot_reply)
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        except Exception as e:
            st.error(f"حدث خطأ: {e}")
