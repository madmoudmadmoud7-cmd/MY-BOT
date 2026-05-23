import streamlit as st
import time

st.set_page_config(page_title="مشروع الذكاء الاصطناعي", layout="centered")

st.title("🤖 مساعدك الذكي للمشاريع")

# تهيئة سجل المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# إدخال المستخدم
if prompt := st.chat_input("اسألني أي شيء عن المشروع..."):
    # عرض سؤال المستخدم
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # رد البوت التلقائي (ديمو)
    with st.chat_message("assistant"):
        with st.spinner("جاري تحليل البيانات..."):
            time.sleep(1.5) # وقت التفكير
            response = "# رد البوت الذكي (ديمو مقنع)
    with st.chat_message("assistant"):
        with st.spinner("جاري قراءة ملف المشروع..."):
            time.sleep(1.5)
            
            # إذا سأل عن الوقت، يجاوب بالوقت
            if "الساعة" in prompt or "الوقت" in prompt:
                from datetime import datetime
                response = f"الساعة الآن هي {datetime.now().strftime('%H:%M')}."
            
            # إذا سأل أي شيء آخر، يجاوب بإجابة تبدو حقيقية من الملف
            else:
                response = (f"بناءً على تحليل ملف المشروع المرفوع، الإجابة على استفسارك حول '{prompt}' هي:\n\n"
                            "1. المخطط المبدئي يوضح أهمية الجدول الزمني المقترح.\n"
                            "2. تم تخصيص الموارد المطلوبة للمرحلة الأولى.\n"
                            "3. المشروع يسير وفقاً للأهداف الموضوعة في المستند.\n\n"
                            "هل تحتاج لتوضيح أي نقطة أخرى من هذه النقاط؟")
            
            st.markdown(response)
            st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
