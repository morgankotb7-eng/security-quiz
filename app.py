import streamlit as st

st.set_page_config(page_title="Cybersecurity Awareness", page_icon="🛡️")

st.title("🛡️ Cybersecurity Awareness Challenge")
st.write("Developed by: **Mohamed Kotb**")
st.divider()

questions = [
    {
        "q": "An urgent email from 'HR' asks for payroll review via (juhayna-portal.net). You:",
        "options": ["Click and log in", "Report it as phishing", "Reply for details"],
        "answer": "Report it as phishing"
    },
    {
        "q": "A common red flag in a phishing email is:",
        "options": ["Professional language", "Extreme urgency or threats", "Mentioning company name"],
        "answer": "Extreme urgency or threats"
    },
    {
        "q": "An IT technician calls and asks for your OTP to 'fix' your account. You:",
        "options": ["Give it to him", "Ask for his ID", "Refuse and hang up"],
        "answer": "Refuse and hang up"
    }
]

score = 0
with st.form("quiz_form"):
    user_answers = []
    for i, item in enumerate(questions):
        st.subheader(f"Question {i+1}")
        ans = st.radio(item["q"], item["options"], key=f"q{i}")
        user_answers.append(ans)
    
    submitted = st.form_submit_button("Submit Results")

if submitted:
    for i, item in enumerate(questions):
        if user_answers[i] == item["answer"]:
            score += 1
    
    st.divider()
    st.header(f"Your Score: {score}/{len(questions)}")
    
    if (score/len(questions)) >= 0.7:
        st.success("Status: [SAFE] ✅ - Good job!")
    else:
        st.error("Status: [HIGH RISK] ⚠️ - Needs more training.")
