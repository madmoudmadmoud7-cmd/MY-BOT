import streamlit as st
from openai import OpenAI

# 1. عنوان التطبيق
st.title("🤖 بوت خدمة العملاء")

# 2. إعداد المفتاح (بدون تعقيدات)
# ارفع هذا الكود، وعندما يطلب منك المربع المفتاح، ضع مفتاحك الجديد فيه
api_key = st.text_input("ضع مفتاح API الخاص بك هنا:", type="password")

if api_key:
    client = OpenAI(api_key=api_key)
    
    # 3. صندوق إدخال السؤال
    user_input = st.text_input("اطرح سؤالك:")
    
    # 4. زر الإرسال
    if st.button("إرسال"):
        if user_input:
            with st.spinner("جاري التفكير..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[{"role": "user", "content": user_input}]
                    )
                    st.success("الرد:")
                    st.write(response.choices[0].message.content)
        else:
            st.warning("يرجى كتابة سؤال.")
else:
    st.info("يرجى إدخال مفتاح  للمتابعة.")
