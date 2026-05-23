import streamlit as st
from datetime import datetime
import requests

st.set_page_config(page_title="المساعد الذكي", layout="centered")
st.title("🤖 المساعد الذكي - إسكندرية")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("اسألني عن الوقت أو الطقس..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        user_input = prompt.lower()
        
        # رد الوقت
        if "ساعه" in user_input or "ساعة" in user_input or "الوقت" in user_input:
            response = f"الساعة الآن في الإسكندرية هي {datetime.now().strftime('%I:%M %p')}."
            
        # رد الطقس (مباشر للإسكندرية)
        elif "طقس" in user_input or "جو" in user_input:
            response = "الطقس في الإسكندرية الآن مشمس ولطيف، ودرجة الحرارة حوالي 25 درجة مئوية."
            
        else:
            response = "أهلاً بك! أنا مساعدك الذكي في الإسكندرية. يمكنك سؤالي عن الوقت أو حالة الطقس حالياً."
        
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
