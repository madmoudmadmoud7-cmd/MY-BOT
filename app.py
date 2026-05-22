import streamlit as st
from openai import OpenAI

# إعداد واجهة المستخدم
st.title("بوت خدمة العملاء (GPT)")

# جلب المفتاح من الإعدادات
# ملاحظة: تأكد من وضع OPENAI_API_KEY في إعدادات Secrets في Streamlit
api_key = st.secrets.get("OPENAI_API_KEY")

if not api_key:
    st.error("لم يتم العثور على المفتاح في إعدادات Secrets.")
else:
    client = OpenAI(api_key=api_key)

    user_input = st.text_input("اطرح سؤالك هنا:")

    if st.button("إرسال"):
        if user_input:
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "أنت مساعد ذكي متخصص في خدمة العملاء."},
                        {"role": "user", "content": user_input}
                    ]
                )
                st.write("الإجابة:")
                st.write(response.choices[0].message.content)
                import gradio as gr
def chat_interface(question):
    return get_bot_response(question, "your_file.pdf")

demo = gr.Interface(fn=chat_interface, inputs="text", outputs="text")
demo.launch()
            except Exception as e:
                st.error(f"حدث 
