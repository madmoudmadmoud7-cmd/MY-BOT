import streamlit as st
import google.generativeai as genai

st.title("البوت الخاص بي")

# محاولة قراءة المفتاح من الـ Secrets
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    
    user_input = st.text_input("اسألني أي شيء:")
    if user_input:
        response = model.generate_content(user_input)
        st.write(response.text)
except Exception as e:
    st.error(f"حدث خطأ: {e}")
    st.write("تأكد أنك وضعت GOOGLE_API_KEY في صفحة الـ Secrets في Streamlit")
