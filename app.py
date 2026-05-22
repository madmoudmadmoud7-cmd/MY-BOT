import streamlit as st
import google.generativeai as genai

st.title("البوت الخاص بي")

# هنجرب نقرأ المفتاح من الـ Secrets
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    if prompt := st.chat_input("اسألني أي شيء:"):
        st.write(model.generate_content(prompt).text)
except Exception as e:
    st.error("المفتاح غير موجود أو غير صحيح، تأكد من إعدادات الـ Secrets")
