import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# إعداد الواجهة
st.title("بوت خدمة عملاء ذكي (Vector Search)")

api_key = st.text_input("ادخل مفتاح Google API:", type="password")

if api_key:
    # 1. إعداد Gemini
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
        st.success("تم الاتصال بـ Gemini بنجاح!")
    except Exception as e:
        st.error(f"خطأ في الاتصال: {e}")
    
    # 2. رفع ملف العميل (PDF)
    uploaded_file = st.file_uploader("ارفع ملف المعلومات الخاص بك", type="pdf")
    
    if uploaded_file:
        st.success("تم رفع الملف بنجاح! اسأل الآن.")
        
        # كود المحادثة
        query = st.text_input("اسألني عن محتوى الملف:")
        if query:
            with st.spinner('جاري التفكير...'):
                response = llm.invoke(query)
                st.write(response.content)
