import streamlit as st
from database.database import insert_user, find_user

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        # Add authentication logic here
        user = find_user(username)
        if user and user["password"] == password:
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password")

def signup():
    st.title("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Sign Up"):
        # Add sign-up logic here
        insert_user(username, password)
        st.success("Account created successfully!")

def main():
    st.sidebar.title("Navigation")
    option = st.sidebar.selectbox("Choose an option", ["Login", "Sign Up"])
    
    if option == "Login":
        login()
    elif option == "Sign Up":
        signup()

if __name__ == "__main__":
    main()