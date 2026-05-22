import streamlit as st
import google.generativeai as genai

# إعداد مفتاح الـ API الخاص بك
genai.configure(api_key="AIzaSyDJHJJt2hluRYLGxMlAPuaN1ShPcDrVdxA")

# إعداد الموديل
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("بوت خدمة العملاء الذكي")

# تهيئة سجل المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
 
# أخذ مدخلات المستخدم
if prompt := st.chat_input("أهلاً بك، كيف يمكنني مساعدتك اليوم؟"):
    st.session_state.messages.append({"role": "user", "content": prompt}) 
    with st.chat_message("user"):
        st.markdown(prompt)

    # الرد عبر Gemini API
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        full_response = response.text
        st.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})