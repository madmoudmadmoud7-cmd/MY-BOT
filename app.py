import streamlit as st
import google.generativeai as genai
import os

# إعداد واجهة المستخدم
st.set_page_config(page_title="بوت خدمة العملاء", page_icon="🤖")
st.title("🤖 بوت خدمة العملاء الذكي")

# محاولة تحميل المفتاح من Streamlit Secrets
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
else:
    st.error("خطأ: لم يتم العثور على GOOGLE_API_KEY في إعدادات الـ Secrets.")
    st.stop()

# إعداد مكتبة جوجل
try:
    genai.configure(api_key=api_key)
    
    # اختيار الموديل (تم تغيير الموديل لـ gemini-1.5-pro لضمان الاستقرار)
    # يمكنك العودة لـ gemini-1.5-flash إذا كان مفتاحك يدعمه في المنطقة الجغرافية الخاصة بك
    model_name = 'gemini-1.5-pro'
    model = genai.GenerativeModel(model_name)
    
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
        message_placeholder = st.empty()
        full_response = ""
        try:
            # استخدام generate_content بطريقة آمنة
            response = model.generate_content(prompt, stream=True)
            
            for chunk in response:
                full_response += chunk.text
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"حدث خطأ أثناء التواصل مع سيرفرات جوجل: {e}")
            st.warning("نصيحة: تأكد من أن الـ API Key الخاص بك مفعل في Google AI Studio وأنه في منطقة جغرافية تدعم هذه النماذج.")
