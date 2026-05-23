import streamlit as st
from datetime import datetime

st.set_page_config(page_title="مساعدك الذكي", layout="centered")

st.title("🤖 المساعد الذكي")

# تهيئة سجل المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# إدخال المستخدم
if prompt := st.chat_input("اكتب سؤالك هنا..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # الرد المنطقي (نظيف وشغال)
    with st.chat_message("assistant"):
        user_input = prompt.lower()
        
        if "الساعة" in user_input or "الوقت" in user_input:
            response = f"الساعة الآن هي {datetime.now().strftime('%H:%M')}، يا فندم."
        elif "ملفاتي" in user_input or "ملفات" in user_input:
            response = "نعم بالطبع، يمكنك رفع ملفاتك وسأقوم بتحليلها ومساعدتك في الإجابة على أي استفسار بخصوصها فوراً."
        else:
            response = "أهلاً بك! أنا مساعدك الذكي، جاهز للإجابة على استفساراتك أو مساعدتك في تحليل ملفاتك. كيف يمكنني خدمتك؟"
        
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
