import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
import os

st.title("بوت خدمة العملاء الذكي")

# 1. إدخال المفتاح
api_key = st.text_input("أدخل Google API Key:", type="password")

if api_key:
    # 2. تعريف الموديل
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
        st.success("تم الاتصال بـ Gemini بنجاح!")
    except Exception as e:
        st.error(f"خطأ في الاتصال: {e}")

    # 3. رفع الملف
    uploaded_file = st.file_uploader("ارفع ملف PDF", type=["pdf"])
    
    if uploaded_file:
        # حفظ الملف مؤقتاً لقراءته
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        loader = PyPDFLoader("temp.pdf")
        pages = loader.load()
        
        # دمج النص من كل الصفحات
        full_text = "\n".join([page.page_content for page in pages])
        st.success("تم قراءة الملف بنجاح! اسألني الآن.")

        # 4. مكان السؤال
        query = st.text_input("اسأل أي شيء عن الملف:")
        
        if query:
            # دمج السؤال مع نص الملف (بدون تعقيد Vector Search مؤقتاً)
            prompt = f"بناءً على المعلومات التالية: {full_text[:10000]} \n\n السؤال: {query}"
            
            try:
                response = llm.invoke(prompt)
                st.write("### الإجابة:")
                st.write(response.content)
            except Exception as e:
                st.error(f"حدث خطأ أثناء الحصول على إجابة: {e}")
