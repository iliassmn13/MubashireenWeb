import streamlit as st

def apply_styles():
    st.markdown(
           """
        <style>
            .team-container {
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
                justify-content: center;
            }
            .team-card {
                flex: 1 0 300px; /* Allow cards to grow, but not shrink below 300px */
                max-width: 100%; /* Ensure cards don't exceed container width */
                border: 2px solid #f0f0f0;
                border-radius: 15px;
                padding: 20px;
                text-align: center;
                background-color: white;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
            .team-card h3 {
                margin: 5px 0;
            }
            .team-card h4 {
                color: #666;
                font-size: 16px;
                margin: 5px 0;
            }
            .team-card p {
                font-size: 14px;
                color: #333;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    apply_styles()
    st.title("Meet Our Team")
    st.write("At Mubashireen, our team is dedicated to providing innovative AI solutions. Here are the key members of our team:")

    team_members = [
        {
            "name": "Zaid Amer",
            "role": "CEO",
            "description": "Zaid leads the company with a vision for innovation and excellence."
        },
        {
            "name": "Amine Labidi",
            "role": "Lead Designer",
            "description": "Amine oversees the technology strategy and development. He is the main designer."
        },
        {
            "name": "Youssif Khalifa",
            "role": "Research Lead",
            "description": "Youssif manages research projects and collaborations."
        },
        {
            "name": "Iliass Bouhsane",
            "role": "HR Manager",
            "description": "Iliass manages the human resources department."
        }
    ]

    # Create a flexbox container for team members
    st.markdown('<div class="team-container">', unsafe_allow_html=True)
    
    for member in team_members:
        st.markdown(
            f"""
            <div class="team-card">
                <h3>{member['name']}</h3>
                <h4>{member['role']}</h4>
                <p>{member['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

"""import streamlit as st
from utils.styles import get_styles, apply_styles

get_styles()

def display_team_member(name, role, image_path, description):
    st.image(image_path, width=150)
    st.subheader(name)
    st.write(f"**Role:** {role}")
    st.write(description)

def main():
    apply_styles()
    st.title("Meet Our Team")
    st.write("At Mubashireen, our team is dedicated to providing innovative AI solutions. Here are the key members of our team:")

    team_members = [
        {
            "name": "Zaid Amer",
            "role": "CEO",
            "description": "Zaid leads the company with a vision for innovation and excellence."
        },
        {
            "name": "Amine Labidi",
            "role": "Lead Designer",
            "description": "Amine oversees the technology strategy and development. He is the main designer."
        },
        {
            "name": "Youssif Khalifa",
            "role": "Research Lead",
            "description": "Youssif manages research projects and collaborations."
        },
         {
            "name": "Iliass Bouhsane",
            "role": "HR Manager",
            "description": "Iliass manages the human resources department."
        }
    ]

    for member in team_members:
        display_team_member(member["name"], member["role"], member["image_path"], member["description"])

if __name__ == "__main__":
    main()"""