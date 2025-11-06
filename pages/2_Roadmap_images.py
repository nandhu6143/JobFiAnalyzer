import streamlit as st

st.title("🚀 Roadmaps for Learning")

# Roadmap image files (replace with actual file paths or URLs)
roadmaps = {
    "Frontend Development": "https://roadmap.sh/roadmaps/frontend.png",
    "Backend Development": "https://roadmap.sh/roadmaps/backend.png",
    "React": "https://roadmap.sh/roadmaps/react.png",
    "Node JS": "https://roadmap.sh/roadmaps/nodejs.png",
    "Python": "https://roadmap.sh/roadmaps/python.png",
    "DevOps": "https://roadmap.sh/roadmaps/devops.png",
    "UX Design": "https://roadmap.sh/roadmaps/ux-design.png",
    "MongoDB": "https://roadmap.sh/roadmaps/mongodb.png",
    "SQL": "https://roadmap.sh/roadmaps/sql.png",
    "BlockChain": "https://roadmap.sh/roadmaps/blockchain.png",
    "Git & Github": "https://roadmap.sh/roadmaps/git-github.png",
}

# Create a grid of clickable cards
cols = st.columns(3)
selected_roadmap = None

for index, (roadmap, img_url) in enumerate(roadmaps.items()):
    with cols[index % 3]:  # This creates a grid layout with 3 cards per row
        if st.button(roadmap):
            selected_roadmap = img_url  # Set the selected roadmap when clicked

# Display the selected roadmap if any
if selected_roadmap:
    st.subheader("Selected Roadmap:")
    st.image(selected_roadmap, use_column_width=True)
else:
    st.info("Click on a roadmap to see its details.")
