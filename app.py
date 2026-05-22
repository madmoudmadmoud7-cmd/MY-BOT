import streamlit as st
from openai import OpenAI

st.title("بوت خدمة العملاء")

# التأكد من وجود المفتاح
if "OPENAI_API_KEY" in st.secrets:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    
    user_input = st.text_input("اسألني أي سؤال:")

    if st.button("إرسال"):
        if user_input:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": user_input}]
            )
            st.write(response.choices[0].message.content)
        else:
            st.warning("يرجى كتابة سؤال.")
else:
    st.error("مفتاح API غير موجود في الإعدادات.")
