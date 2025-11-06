import streamlit as st

st.title("Skills and Learning Videos")

# Skill names and corresponding YouTube links
skills = {
    "JAVA": "https://youtu.be/yRpLlJmRo2w?si=aEwwMno_CUQTr1Wk",
    "Web Development": "https://youtu.be/tVzUXW6siu0?si=Rva8TGDWWXa_h5vQ",
    "React Js": "https://youtu.be/b9eMGE7QtTk?si=TLXj46qIVCZFXUvi",
    "Node Js": "https://youtu.be/ohIAiuHMKMI?si=4-Xvrw8hbDct93cI",
    "Dsa": "https://youtu.be/h3uDCJ5mvgw?si=keWormhAznjBqW9d",
    "Material UI": "https://youtu.be/0KEpWHtG10M?si=gjzUGOhm-C6-mGvj",
    "C": "https://www.youtube.com/watch?v=KJgsSFOSQv0",
    "C++": "https://www.youtube.com/watch?v=vLnPwxZdW4Y",
    "PHP": "https://www.youtube.com/watch?v=OK_JCtrrv-c",
}



# Convert skills dictionary into a list of items
skill_items = list(skills.items())

# Display skills in pairs of two (two cards in one row)
for i in range(0, len(skill_items), 2):
    cols = st.columns(2)  # Create two columns
    
    # For the first column
    with cols[0]:
        skill, link = skill_items[i]
        st.subheader(skill)
        st.video(link)
    
    # For the second column (if available)
    if i + 1 < len(skill_items):
        with cols[1]:
            skill, link = skill_items[i + 1]
            st.subheader(skill)
            st.video(link)
