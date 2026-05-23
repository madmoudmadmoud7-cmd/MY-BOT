import streamlit as st

st.set_page_config(page_title="المساعد الذكي", layout="centered")
st.title("🤖 المساعد الذكي - ديمو نهائي")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("اسألني عن الأكلة أو الوقت..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        user_input = prompt.lower()
        
        # 1. رد الوقت المطلوب
        if "ساعه" in user_input or "ساعة" in user_input or "الوقت" in user_input:
            response = "الساعة الآن 08:16 صباحاً يا فندم."
            
        # 2. رد أكلة الكبسة
        elif "اكل" in user_input or "اكلة" in user_input or "غداء" in user_input:
            response = """أقترح عليك اليوم تناول الكبسة السعودية! 🥘

### فوائد الكبسة:
* طاقة عالية: تمد الجسم بالبروتين اللازم بفضل الدجاج أو اللحم.
* تحسين الهضم: تحتوي على توابل طبيعية مفيدة للجهاز الهضمي.
* مذاق فريد: تُعتبر من أشهى الأطباق المتكاملة والمشبعة.

بالهناء والشفاء!"""
        
        else:
            response = "أهلاً بك! أنا مساعدك الذكي. اسألني عن 'الساعة' أو 'اقتراح لأكلة اليوم'."
        
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
