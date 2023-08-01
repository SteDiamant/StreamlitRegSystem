import streamlit as st
from database import User
import pandas as pd
from MontlyReport import main as ds_main
from Comparator import main as comp_main
dashboard = st.container()
headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()
registrationSection = st.container()
comparatorSection = st.container()
pagesMenuSection = st.container()
# Implement your login and user authentication logic here.
# Replace the function `login()` with your own implementation.
# For example, you could use a database to verify credentials.
def login(username, password):
    # Replace this with your authentication logic.
    user = User.login_user(username, password)
    if user:
        return True
    else:
        return False
def show_dashboard_page():
    with dashboard:
        st.title("Dashboard")
        ds_main()

def show_main_page():
    with mainSection:
        dataFile = st.text_input("Enter your Test file name: ")
        Topics = st.text_input("Enter your Model Name: ")
        ModelVersion = st.text_input("Enter your Model Version: ")
        processingClicked = st.button("Start Processing", key="processing")
        if processingClicked:
            st.balloons()


def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False


def show_logout_page():
    loginSection.empty()
    with logOutSection:
        st.sidebar.button("Log Out", key="logout", on_click=LoggedOut_Clicked)


def LoggedIn_Clicked(userName, password):
    if login(userName, password):
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False
        st.error("Invalid user name or password")


def show_login_page():
    with loginSection:
        if not st.session_state['loggedIn']:
            userName = st.sidebar.text_input(label="", value="", placeholder="Enter your user name", key="userName_login")
            password = st.sidebar.text_input(label="", value="", placeholder="Enter password", type="password", key="password_login")
            st.sidebar.button("Login", on_click=LoggedIn_Clicked, args=(userName, password))


def registrationSection_page():
    name = st.sidebar.text_input("Username")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")
    verify_password = st.sidebar.text_input("Verify Password", type="password")
    
    submit_button = st.sidebar.button('Register')
    if submit_button:
        if password == verify_password:
            User.register_user(name, password, email)
            st.success("Registration successful. Please log in.")
            st.balloons()
        else:
            st.error("Passwords do not match. Please try again.")


def show_users_db():  
    users = User.all_users()
    st.title("Update Information")
    if users is not None:
        # Allow the user to update information
        selected_user = st.selectbox("Select a user", [user[1] for user in users])
        new_username = st.text_input("Update Username")
        update_button = st.button("Update")
        if update_button:
            if User.update_user_info(selected_user, new_username):
                st.success("Information updated successfully.")
            else:
                st.error("Error occurred while updating information.")

        # Find the selected user's email
        selected_user_info = [user for user in users if user[1] == selected_user]
        if len(selected_user_info) > 0:
            selected_email = selected_user_info[0][3]
        else:
            selected_email = ""

        update_email = st.text_input("Update Email", placeholder=selected_email)
        if st.button("Update Email", key='update_email'):
            User.update_email(selected_user, update_email)

        delete_button = st.button("Delete User")
        if delete_button:
            if User.delete_user(selected_user):
                st.success("User deleted successfully.")
            else:
                st.error("Error occurred while deleting user.")

    if st.button("Delete Empty Usernames", key='delete_empty_usernames'):
        User.delete_empty_usernames()
  
def show_comparator_page():
    with comparatorSection:
        st.title("Comparator")
        comp_main()


def show_pages_menu():
        st.sidebar.title("Menu")
        selection = st.sidebar.radio("Go to", ["Update Information", "Montly Overview", "Comparator Tool"])
        if selection == "Update Information":
            show_users_db()
        elif selection == "Montly Overview":
            show_dashboard_page()
        elif selection == "Comparator Tool":
            show_comparator_page()
        else:
            st.title("Home Page")
            st.write("Welcome to the home page!")




def main():
    
    menu_selection = st.sidebar.radio("Menu", ["Register", "Login"],key="menu")

    if menu_selection == "Register":
            registrationSection_page()

    else:  # "Login" is selected
        if 'loggedIn' not in st.session_state:
            st.session_state['loggedIn'] = False
        if st.session_state['loggedIn']:
            show_logout_page()
            show_pages_menu()
        else:
            show_login_page()
    

if __name__ == "__main__":
    main()
