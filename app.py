import streamlit as st
import time

st.set_page_config(page_title="مشروع الذكاء الاصطناعي", layout="centered")

st.title("🤖 مساعدك الذكي للمشاريع")

# تهيئة سجل المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# إدخال المستخدم
if prompt := st.chat_input("اسألني أي شيء عن المشروع..."):
    # عرض سؤال المستخدم
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # رد البوت التلقائي (ديمو)
    with st.chat_message("assistant"):
        with st.spinner("جاري تحليل البيانات..."):
            time.sleep(1.5) # وقت التفكير
            response = "بناءً على المعلومات المتاحة في ملف المشروع، هذا الاستفسار دقيق جداً. يمكننا المضي قدماً في تنفيذ هذا الجزء من المخطط. هل لديك أي استفسار آخر؟"
            st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
