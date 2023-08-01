import streamlit as st
import sqlite3
import hashlib

def create_users_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL ,
            password TEXT NOT NULL ,
            email TEXT NOT NULL ,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            
            
        )
    """)
    conn.commit()
    conn.close()

class User():
    @staticmethod
    def delete_user(username):
        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE username=?", (username,))
            conn.commit()
            conn.close()
            st.experimental_rerun()
            return True
        except sqlite3.Error as e:
            print("Error occurred during database drop:", e)
            return False


    @staticmethod
    def update_user_info(username, new_info):
        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()

            # Execute the update statement
            query = f"UPDATE users SET username=? WHERE username=?"
            cursor.execute(query, (new_info, username))

            # Commit the changes
            conn.commit()

            # Close the connection
            conn.close()

            return True
        except sqlite3.Error as e:
            print("Error occurred during database update:", e)
            return False

    @staticmethod
    def delete_empty_usernames():
        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE username = ''")
            conn.commit()
            conn.close()
            st.experimental_rerun()
            return True
        except sqlite3.Error as e:
            print("Error occurred during database drop:", e)
            return False
        
    @staticmethod
    def update_email(username,newemail):
        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()

            # Execute the update statement
            query = f"UPDATE users SET email=? WHERE username=?"
            cursor.execute(query, (newemail, username))

            # Commit the changes
            conn.commit()

            # Close the connection
            conn.close()

            return True
        except sqlite3.Error as e:
            print("Error occurred during database update:", e)
            return False
    @staticmethod
    def all_users():
        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            conn.close()
            return users
        except sqlite3.Error as e:
            print("Error occurred during fetching users:", e)
            return None
        
    @staticmethod
    def register_user(username, password, email):
        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()

            # Check if the email already exists in the database
            cursor.execute("SELECT * FROM users WHERE email=?", (email,))
            existing_user = cursor.fetchone()
            if existing_user:
                conn.close()
                return False, "Email already registered. Please use a different email."

            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, hashed_password, email))
            conn.commit()
            conn.close()
            return True, "Registration successful. Please log in."
        except sqlite3.Error as e:
            print("Error occurred during user registration:", e)
            return False, "An error occurred during registration. Please try again later."

    @staticmethod
    def login_user(username, password):
        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
            user = cursor.fetchone()
            conn.close()
            return user
        except sqlite3.Error as e:
            print("Error occurred during user login:", e)
            return None