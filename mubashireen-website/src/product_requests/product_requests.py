import streamlit as st
from database.database import insert_project_request

def product_request_form():
    st.title("Comments and Suggestions")
# Initialize session state for form inputs
    if 'name' not in st.session_state:
        st.session_state.name = ""
    if 'email' not in st.session_state:
        st.session_state.email = ""
    if 'project_details' not in st.session_state:
        st.session_state.project_details = ""
    
    # Create form inputs
"""    st.session_state.name = st.text_input("Name", value=st.session_state.name)
    st.session_state.email = st.text_input("Email", value=st.session_state.email)
    st.session_state.project_details = st.text_area("Comments and Suggestions", value=st.session_state.project_details)
    
    if st.button("Submit Comments"):
        request_data = {
            "name": st.session_state.name,
            "email": st.session_state.email,
            "project_details": st.session_state.project_details
       }
        insert_project_request(request_data)
        st.success("Request submitted successfully!")
        st.session_state.name = ""
        st.session_state.email = ""
        st.session_state.project_details = """""

with st.form("my_form"):
        name = st.text_input("Enter your name:", value=st.session_state.name)
        email = st.text_input("Enter your email:", value=st.session_state.email)
        project_details = st.text_area("Enter your comments and suggestions:", value=st.session_state.project_details)

if st.form_submit_button("Submit"):
            request_data = {
                "name": st.session_state.name,
                "email": st.session_state.email,
                "project_details": st.session_state.project_details
            }
            insert_project_request(request_data)
            st.success("Request submitted successfully!")
            st.session_state.name = ""
            st.session_state.email = ""
            st.session_state.project_details = ""

if __name__ == "__main__":
    product_request_form()
