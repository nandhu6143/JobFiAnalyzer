import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json


# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Google Generative AI (Gemini)
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# Function to extract text from PDF file
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        text += str(reader.pages[page].extract_text())
    return text

# Prompt Templates
input_prompt_template = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of the tech field, software engineering, data science, data analysis,
and big data engineering. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide
the best assistance for improving the resumes. Assign the percentage Matching based
on the JD and
the missing keywords with high accuracy.
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

improvement_prompt_template = """
You are an experienced ATS and career advisor. Provide actionable feedback on how the candidate
can improve their resume to better match the job description. Include specific keywords, skills,
and experiences that should be added or emphasized.
resume:{text}
description:{jd}
"""

overview_prompt_template = """
You are a skilled career advisor. Provide a brief summary of the candidate's resume in 30 lines.
resume:{text}
"""

# Streamlit App Design
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Job Fit Analyzer🚀</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>Improve your resume with cutting-edge AI analysis</p>", unsafe_allow_html=True)

# Job description input
st.markdown("### 📄 Paste the Job Description")
jd = st.text_area("Paste the Job Description here", height=200)

# Resume file upload
st.markdown("### 📤 Upload Your Resume (PDF)")
uploaded_file = st.file_uploader("Upload your resume in PDF format", type="pdf", help="Please upload the PDF")

# Action Buttons
st.markdown("### 🔎 Choose an Action:")
col1, col2, col3, col4 = st.columns(4)

with col1:
    submit1 = st.button("📋 Tell Me About the Resume")

with col2:
    submit = st.button("📊 Percentage Match")

with col3:
    submit2 = st.button("🛠️ Improvement Suggestions")

with col4:
    submit3 = st.button("🔍 Overview (30 Lines)")

# Processing the resume file
if uploaded_file is not None:
    text = input_pdf_text(uploaded_file)
    
    # If "Tell Me About the Resume" button is clicked
    if submit1:
        input_prompt = overview_prompt_template.format(text=text)
        response = get_gemini_response(input_prompt)
        st.markdown("<h2 style='color: #4CAF50;'>Resume Overview</h2>", unsafe_allow_html=True)
        st.write(response)

    # If "Percentage Match" button is clicked
    if submit:
        input_prompt = input_prompt_template.format(text=text, jd=jd)
        response = get_gemini_response(input_prompt)
        response_json = json.loads(response)
        
        st.markdown("<h2 style='color: #4CAF50;'>Evaluation Result</h2>", unsafe_allow_html=True)
        st.markdown(f"**📈 JD Match:** `{response_json['JD Match']}`")
        st.markdown("**🔑 Missing Keywords:**")
        st.markdown("<ul>", unsafe_allow_html=True)
        for keyword in response_json["MissingKeywords"]:
            st.markdown(f"<li>{keyword}</li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)
        st.markdown("**📋 Profile Summary:**")
        st.write(response_json["Profile Summary"])

    # If "Improvement Suggestions" button is clicked
    if submit2:
        input_prompt = improvement_prompt_template.format(text=text, jd=jd)
        response = get_gemini_response(input_prompt)
        st.markdown("<h2 style='color: #4CAF50;'>Improvement Suggestions</h2>", unsafe_allow_html=True)
        st.write(response)

    # If "Overview (30 Lines)" button is clicked
    if submit3:
        input_prompt = overview_prompt_template.format(text=text)
        response = get_gemini_response(input_prompt)
        st.markdown("<h2 style='color: #4CAF50;'>Resume Overview (30 Lines)</h2>", unsafe_allow_html=True)
        st.write(response)

else:
    st.info("Please upload a resume in PDF format to begin.")
