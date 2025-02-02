import streamlit as st

def display_projects():
    st.title("Our Projects")
    st.write("Explore our innovative projects that are designed to aid and guide various industries.")

    projects = [
        {
            "title": "Warehouse Helper",
            "description": "An AI-powered assistant to streamline warehouse operations and increase efficiency."
        },
        {
            "title": "Firefighter Guider",
            "description": "A cutting-edge solution to assist firefighters in navigating dangerous environments safely."
        }
    ]

    for project in projects:
        st.subheader(project["title"])
        st.write(project["description"])

if __name__ == "__main__":
    display_projects()
