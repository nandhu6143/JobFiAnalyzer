import streamlit as st

st.write("heello")
x=st.text_input("Enter something")
st.write(f"Entered elem was {x}")


st.page_link("pages/1_Skills_videos.py", label="Page 1", icon="1️⃣")
st.page_link("pages/2_Roadmap_images.py", label="Page 2", icon="2️⃣")
st.page_link("http://www.google.com", label="Google", icon="🌎")