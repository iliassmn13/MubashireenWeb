import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from projects.projects import display_projects
from team.team import main as team_main

st.set_page_config(
    page_title="Main - Mubashireen",
    page_icon="🕌", 
    layout="wide"
)
st.markdown(
        """
<style>
 .stApp {
    background-image: url("https://i.pinimg.com/1200x/84/2a/d6/842ad68b315b0f586c30b465221da609.jpg");
    background-size: cover;
    background-repeat: repeat;
}
</style>
        """,
        unsafe_allow_html=True
    )
custom_css = """
<style>
    [data-testid="stSidebar"] {
        background-color: #ccffcc !important; /* Light green */
    }
</style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)
def main_page():
    # Create a div for the main content
    st.markdown('<div class="main-page">', unsafe_allow_html=True)
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
def sidebar_navigation():
    # Move the title to the top of the sidebar
    st.sidebar.title("Navigation")

    # Style for the sidebar buttons
    st.sidebar.markdown(
        """<style>
                .sidebar-buttons {
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                }
                .stButton button {
                    width: 100%;
                    background-color: #008000;
                    color: white;
                    border-radius: 10px;
                    padding: 8px;
                    font-size: 16px;
                    border: none;
                }
                .stButton button:hover {
                    background-color: #003080;
                }
        </style>""",
        unsafe_allow_html=True
    )

    home_button = st.sidebar.button("🏠 Home")
    projects_button = st.sidebar.button("🚀 Services in offer")
    team_button = st.sidebar.button("👥 Team")
    # Match button clicks
    if home_button:
        page = "Home"
    elif projects_button:
        page = "Services in offer"
    elif team_button:
        page = "Team"
    else:
        return "Home"

# Return the selected page
    return page

st.sidebar.markdown('</div>', unsafe_allow_html=True)

def main():
    main_page()
option = sidebar_navigation()
if option == "Home":
        st.title("Welcome to Mubashireen")
        st.subheader("Your Source for Good News")
        
        description = (
            "At Mubashireen, our mission is to provide good news through innovative AI solutions. "
            "We strive to empower our clients with tools that enhance their productivity and decision-making. "
            "Join us on our journey to spread positivity and efficiency in the digital world."
        )
        
        st.write(description)
        st.markdown("[🌐 A Presentation of who we are](https://docs.google.com/presentation/d/18d6BMFkw6xkPo5hLfjvRXNf9Afev3LBg0O6DuUyhzmE/edit?usp=sharing)", unsafe_allow_html=True)
elif option == "Services in offer":
        display_projects()
elif option == "Team":
        team_main()
        
if __name__ == "__main__":
    main()