import streamlit as st

st.title("💼 Tips and Tricks for Creating Resumes")

# List of tips for improving resumes
tips = [
    {
        "title": "Use Strong Action Verbs 🚀",
        "content": "Start your bullet points with action verbs like 'Developed', 'Led', 'Managed', or 'Initiated' to show what you actively contributed."
    },
    {
        "title": "Tailor Your Resume 📝",
        "content": "Customize your resume for every job application. Align your experience and skills to the specific job description you're applying for."
    },
    {
        "title": "Keep It Concise 📏",
        "content": "Limit your resume to 1-2 pages. Recruiters spend less than a minute reviewing each resume, so make sure the key information stands out."
    },
    {
        "title": "Highlight Key Experience 🔝",
        "content": "Place your most relevant experience at the top of your resume. This ensures that your most impressive accomplishments are seen first."
    },
    {
        "title": "Quantify Your Achievements 📊",
        "content": "Whenever possible, use numbers to demonstrate the impact of your work. For example, 'Increased sales by 30%' or 'Reduced costs by 15%'."
    },
    {
        "title": "Optimize for Keywords 🔑",
        "content": "Incorporate keywords from the job description into your resume, especially in the skills and experience sections. This helps in ATS (Applicant Tracking System) screening."
    },
    {
        "title": "Use Clean Formatting 📄",
        "content": "Ensure consistent font sizes and spacing. Use a professional format, and make sure your resume is easy to read both on-screen and in print."
    },
    {
        "title": "Include Certifications 🏅",
        "content": "Add any certifications relevant to the job you're applying for. This adds credibility and showcases your expertise in specialized areas."
    },
    {
        "title": "Showcase Your Soft Skills 🤝",
        "content": "Incorporate examples of teamwork, leadership, communication, and problem-solving skills in your work experience or summary."
    },
    {
        "title": "Add a Professional Summary 📋",
        "content": "At the top of your resume, add a brief summary that highlights your qualifications, key skills, and what makes you a great fit for the role."
    }
]

# Display each tip in a card-style format
for tip in tips:
    with st.container():
        st.markdown(f"### {tip['title']}")
        st.markdown(f"{tip['content']}")
        st.markdown("---")
