import streamlit as st
from groq import Groq

st.title("🤖 بوت خدمة العملاء (Groq)")

# قراءة المفتاح من الـ Secrets
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    
    user_input = st.text_input("اسألني أي سؤال:")
    if st.button("إرسال"):
        if user_input:
            with st.spinner("جاري التفكير..."):
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": user_input}],
                    model="llama3-8b-8192",
                )
                st.success("الرد:")
                st.write(chat_completion.choices[0].message.content)
        else:
            st.warning("يرجى كتابة سؤال.")
except Exception as e:
    
