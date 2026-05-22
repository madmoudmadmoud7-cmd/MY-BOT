import streamlit as st
import google.generativeai as genai
import os

# إعداد واجهة المستخدم
st.set_page_config(page_title="بوت خدمة العملاء", page_icon="🤖")
st.title("🤖 بوت خدمة العملاء الذكي")

# محاولة تحميل المفتاح من Streamlit Secrets
# تأكد أن اسم المتغير في صفحة Secrets هو بالضبط: GOOGLE_API_KEY
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
else:
    st.error("خطأ: لم يتم العثور على GOOGLE_API_KEY في إعدادات الـ Secrets. يرجى إضافته.")
    st.stop()

# إعداد مكتبة جوجل
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"خطأ في إعداد نموذج الذكاء الاصطناعي: {e}")
    st.stop()

# تهيئة سجل المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال رسالة المستخدم
if prompt := st.chat_input("كيف يمكنني مساعدتك اليوم؟"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # الرد من جوجل
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            full_response = response.text
            st.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error(f"حدث خطأ أثناء التواصل مع جوجل: {e}")
