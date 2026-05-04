import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="Juhayna Cyber-Challenge", page_icon="🛡️", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stRadio > label { font-weight: bold; color: #1e3a8a; }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #004a99;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Corporate Cybersecurity Assessment")
st.subheader("Test Your Defense Readiness")
st.write("Prepared by: **Mohamed Kotb** | IT Operations Lead")
st.divider()

# 10 Professional & Engaging Questions
questions = [
    {
        "q": "1. You receive an email from 'IT-Support' with a PDF titled 'New Salary Scale 2026'. The sender's email is 'support@juhayna-office.com'. What is your first action?",
        "options": ["Open the PDF immediately", "Check with Mohamed Kotb or the IT team first", "Forward it to all my colleagues"],
        "answer": "Check with Mohamed Kotb or the IT team first",
        "feedback": "Correct. Unexpected attachments about sensitive topics like salaries are major red flags."
    },
    {
        "q": "2. An automated call (Robocall) claims your work account will be locked in 1 hour unless you press '1' to speak to an agent. You should:",
        "options": ["Press 1 to fix it", "Hang up. Official IT alerts don't come via suspicious robocalls.", "Give them my password to verify identity"],
        "answer": "Hang up. Official IT alerts don't come via suspicious robocalls.",
        "feedback": "Correct. This is a Vishing (Voice Phishing) attack."
    },
    {
        "q": "3. You are working from a coffee shop. Which Wi-Fi is safer for company business?",
        "options": ["'Free_Coffee_WiFi' (Open)", "My personal mobile hotspot with a strong password", "Any network that has a 5-star signal"],
        "answer": "My personal mobile hotspot with a strong password",
        "feedback": "Correct. Public Wi-Fi is a playground for hackers."
    },
    {
        "q": "4. [The 'Polite' Joke] You found a very high-quality USB drive on the office floor. What's the protocol?",
        "options": ["Plug it in to see if it has my favorite movies", "Submit it to the IT Desk immediately", "Keep it, it's my lucky day!"],
        "answer": "Submit it to the IT Desk immediately",
        "feedback": "Correct! USB drives can contain 'Rubber Ducky' scripts that hack your PC in seconds."
    },
    {
        "q": "5. A WhatsApp message from an unknown international number says: 'Hello, I'm the CEO. I need you to buy 5 iTunes gift cards for a client.' You:",
        "options": ["Buy them to impress the CEO", "Block the number. Our CEO won't ask for gift cards on WhatsApp.", "Ask him which flavor of iTunes cards he likes"],
        "answer": "Block the number. Our CEO won't ask for gift cards on WhatsApp.",
        "feedback": "Correct. This is a classic 'CEO Fraud' scam."
    },
    {
        "q": "6. Why is it dangerous to post a photo of your work ID badge on LinkedIn?",
        "options": ["The photo might look bad", "Hackers can clone the barcode or use my info for social engineering", "Company policy says I'm not famous enough"],
        "answer": "Hackers can clone the barcode or use my info for social engineering",
        "feedback": "Correct. Your badge is for the office, not for social media."
    },
    {
        "q": "7. You receive an MFA (OTP) code on your phone that you DID NOT request. What does this mean?",
        "options": ["My phone is broken", "Someone knows my password and is trying to log in", "It's just a system glitch, ignore it"],
        "answer": "Someone knows my password and is trying to log in",
        "feedback": "Correct. Change your password immediately if this happens!"
    },
    {
        "q": "8. [Hard Scenario] You get an email from a real supplier you know, but the IBAN for payment has changed 'due to an audit'. You should:",
        "options": ["Update the IBAN and pay", "Call the supplier on their KNOWN official number to verify", "Reply to the email and ask if they are sure"],
        "answer": "Call the supplier on their KNOWN official number to verify",
        "feedback": "Correct! This is Business Email Compromise (BEC)."
    },
    {
        "q": "9. A 'Cleaners' crew you don't recognize enters a secure zone without badging in. They are carrying heavy tools. You:",
        "options": ["Hold the door for them to be polite", "Ask them to badge in or contact Security/IT Desk", "Assume they are new employees"],
        "answer": "Ask them to badge in or contact Security/IT Desk",
        "feedback": "Correct. Physical security is the first line of defense."
    },
    {
        "q": "10. [Final Question] What is the most important rule in Cybersecurity?",
        "options": ["Trust everyone", "Never click suspicious links and always report anomalies", "Only IT people need to worry about security"],
        "answer": "Never click suspicious links and always report anomalies",
        "feedback": "Correct! Security is everyone's responsibility."
    }
]

# Quiz State logic
if 'score' not in st.session_state:
    st.session_state.score = 0

with st.form("quiz_form"):
    user_answers = []
    for i, item in enumerate(questions):
        st.markdown(f"**Question {i+1}:** {item['q']}")
        ans = st.radio("Choose one:", item["options"], key=f"q{i}", index=None)
        user_answers.append(ans)
        st.write("---")

    submitted = st.form_submit_button("Submit Assessment")

if submitted:
    if None in user_answers:
        st.warning("⚠️ Please complete all 10 questions before submitting.")
    else:
        score = 0
        for i, item in enumerate(questions):
            if user_answers[i] == item["answer"]:
                score += 1
            else:
                st.error(f"❌ Q{i+1} was wrong. {item['feedback']}")
        
        st.divider()
        final_pct = (score / len(questions)) * 100
        
        if final_pct >= 90:
            st.balloons()
            st.success(f"🏆 Score: {score}/10 - Expert Level! You are a Security Champion.")
        elif final_pct >= 70:
            st.warning(f"🥈 Score: {score}/10 - Good, but stay vigilant.")
        else:
            st.error(f"🚨 Score: {score}/10 - High Risk! Please attend the next IT Security briefing.")

st.caption("© 2026 | Developed for Juhayna Excellence by Mohamed Kotb")
