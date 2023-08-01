import streamlit as st
import sqlite3
import hashlib


def create_users_table():
    """
    Create the 'users' table in the database if it doesn't exist.

    The table will have the following columns:
        - id: INTEGER (Primary Key, Autoincrement)
        - username: TEXT (Not NULL)
        - password: TEXT (Not NULL)
        - email: TEXT (Not NULL)
        - created_at: TIMESTAMP (Default CURRENT_TIMESTAMP)

    Returns:
        None
    """
    try:
        # Establish a connection to the database using a context manager (with statement).
        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()

            # Execute the CREATE TABLE statement to create the 'users' table if it doesn't exist.
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Commit the changes to the database.
            conn.commit()

    except sqlite3.Error as e:
        # If an SQLite error occurs during table creation, catch the exception and handle it.
        # Print the error for debugging purposes.
        print("Error occurred during table creation:", e)

class User():
    @staticmethod
    def delete_user(username):
        """
        Delete a user from the database.

        Parameters:
            username (str): The username of the user to delete.

        Returns:
            bool: True if the user is deleted successfully, False otherwise.
        """
        try:
            # Establish a connection to the database using a context manager (with statement).
            with sqlite3.connect("users.db") as conn:
                cursor = conn.cursor()

                # Execute the DELETE query with a parameterized query to avoid SQL injection.
                cursor.execute("DELETE FROM users WHERE username=?", (username,))
                
                # Commit the changes to the database.
                conn.commit()

            # Close the connection explicitly (though not strictly necessary with a context manager).
            # This helps ensure timely release of resources.
            # Note: SQLite automatically closes the connection when the script exits, but it's good practice to do it explicitly.
            conn.close()

            # Trigger a Streamlit rerun to update the UI after deletion.
            st.experimental_rerun()

            # Return True, indicating successful deletion.
            return True

        except sqlite3.Error as e:
            # If an SQLite error occurs during the deletion process, catch the exception and handle it.
            # Print the error for debugging purposes.
            print("Error occurred during database drop:", e)

            # Return False, indicating deletion was unsuccessful.
            return False

    @staticmethod
    def update_user_info(username, new_info):
        """
        Update the user information in the database.

        Parameters:
            username (str): The username of the user to update.
            new_info (str): The new information to update for the user.

        Returns:
            bool: True if the user information is updated successfully, False otherwise.
        """
        try:
            # Establish a connection to the database using a context manager (with statement).
            with sqlite3.connect("users.db") as conn:
                cursor = conn.cursor()

                # Execute the update statement with parameterized query to avoid SQL injection.
                query = "UPDATE users SET username=? WHERE username=?"
                cursor.execute(query, (new_info, username))

                # Commit the changes to the database.
                conn.commit()

            # Close the connection explicitly (though not strictly necessary with a context manager).
            # This helps ensure timely release of resources.
            # Note: SQLite automatically closes the connection when the script exits, but it's good practice to do it explicitly.
            conn.close()

            # Return True, indicating successful update.
            return True

        except sqlite3.Error as e:
            # If an SQLite error occurs during the update process, catch the exception and handle it.
            # Print the error for debugging purposes.
            print("Error occurred during database update:", e)

            # Return False, indicating update was unsuccessful.
            return False

    @staticmethod
    def delete_empty_usernames():
        """
        Delete users with empty usernames from the database.

        Returns:
            bool: True if empty usernames are deleted successfully, False otherwise.
        """
        try:
            # Establish a connection to the database using a context manager (with statement).
            with sqlite3.connect("users.db") as conn:
                cursor = conn.cursor()

                # Execute the DELETE query to remove rows with empty usernames.
                cursor.execute("DELETE FROM users WHERE username = ''")
                
                # Commit the changes to the database.
                conn.commit()

            # Close the connection explicitly (though not strictly necessary with a context manager).
            # This helps ensure timely release of resources.
            # Note: SQLite automatically closes the connection when the script exits, but it's good practice to do it explicitly.
            conn.close()

            # Trigger a Streamlit rerun to update the UI after deletion.
            st.experimental_rerun()

            # Return True, indicating successful deletion of empty usernames.
            return True

        except sqlite3.Error as e:
            # If an SQLite error occurs during the deletion process, catch the exception and handle it.
            # Print the error for debugging purposes.
            print("Error occurred during database drop:", e)

            # Return False, indicating deletion was unsuccessful.
            return False
 
    @staticmethod
    def update_email(username, newemail):
        """
        Update the email of a user in the database.

        Parameters:
            username (str): The username of the user whose email needs to be updated.
            newemail (str): The new email to update for the user.

        Returns:
            bool: True if the email is updated successfully, False otherwise.
        """
        try:
            # Establish a connection to the database using a context manager (with statement).
            with sqlite3.connect("users.db") as conn:
                cursor = conn.cursor()

                # Execute the update statement with a parameterized query to avoid SQL injection.
                query = "UPDATE users SET email=? WHERE username=?"
                cursor.execute(query, (newemail, username))

                # Commit the changes to the database.
                conn.commit()

            # Close the connection explicitly (though not strictly necessary with a context manager).
            # This helps ensure timely release of resources.
            # Note: SQLite automatically closes the connection when the script exits, but it's good practice to do it explicitly.
            conn.close()

            # Return True, indicating successful email update.
            return True

        except sqlite3.Error as e:
            # If an SQLite error occurs during the update process, catch the exception and handle it.
            # Print the error for debugging purposes.
            print("Error occurred during database update:", e)

            # Return False, indicating the email update was unsuccessful.
            return False

    @staticmethod
    def all_users():
        """
        Retrieve all users from the database.

        Returns:
            list: A list of tuples containing user information (username, password, email).
                  Returns None if an error occurs during the fetching process.
        """
        try:
            # Establish a connection to the database using a context manager (with statement).
            with sqlite3.connect("users.db") as conn:
                cursor = conn.cursor()

                # Execute the SELECT query to retrieve all users from the database.
                cursor.execute("SELECT * FROM users")
                users = cursor.fetchall()

            # Return the list of users.
            return users

        except sqlite3.Error as e:
            # If an SQLite error occurs during the fetching process, catch the exception and handle it.
            # Print the error for debugging purposes.
            print("Error occurred during fetching users:", e)

            # Return None to indicate an error occurred during the operation.
            return None
        
    @staticmethod
    def register_user(username, password, email):
        """
        Register a new user in the database.

        Parameters:
            username (str): The username of the new user.
            password (str): The password of the new user (plaintext).
            email (str): The email of the new user.

        Returns:
            tuple: A tuple containing two values:
                - bool: True if registration is successful, False otherwise.
                - str: A message indicating the result of the registration process.
        """
        try:
            # Establish a connection to the database using a context manager (with statement).
            with sqlite3.connect("users.db") as conn:
                cursor = conn.cursor()

                # Check if the email already exists in the database.
                cursor.execute("SELECT * FROM users WHERE email=?", (email,))
                existing_user = cursor.fetchone()
                if existing_user:
                    # If the email is already registered, close the connection and return an error message.
                    return False, "Email already registered. Please use a different email."

                # Hash the password using SHA-256 before storing it in the database.
                hashed_password = hashlib.sha256(password.encode()).hexdigest()

                # Execute the INSERT query to add the new user to the database.
                cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                               (username, hashed_password, email))

                # Commit the changes to the database.
                conn.commit()

            # Return True and a success message indicating the registration was successful.
            return True, "Registration successful. Please log in."

        except sqlite3.Error as e:
            # If an SQLite error occurs during the registration process, catch the exception and handle it.
            # Print the error for debugging purposes.
            print("Error occurred during user registration:", e)

            # Return False and an error message indicating the registration was unsuccessful.
            return False, "An error occurred during registration. Please try again later."

    @staticmethod
    def login_user(username, password):
        """
        Authenticate a user during login.

        Parameters:
            username (str): The username of the user trying to log in.
            password (str): The password provided by the user (plaintext).

        Returns:
            tuple: A tuple containing user information (username, password, email) if login is successful.
                   Returns None if an error occurs during the login process or if authentication fails.
        """
        try:
            # Establish a connection to the database using a context manager (with statement).
            with sqlite3.connect("users.db") as conn:
                cursor = conn.cursor()

                # Hash the provided password using SHA-256 to match with the hashed password in the database.
                hashed_password = hashlib.sha256(password.encode()).hexdigest()

                # Execute the SELECT query to find a user with matching username and password.
                cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                               (username, hashed_password))
                user = cursor.fetchone()

            # Return the user information if login is successful.
            return user

        except sqlite3.Error as e:
            # If an SQLite error occurs during the login process, catch the exception and handle it.
            # Print the error for debugging purposes.
            print("Error occurred during user login:", e)

            # Return None to indicate an error occurred during the operation.
            return None
