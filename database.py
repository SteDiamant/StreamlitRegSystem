
import streamlit as st
import sqlite3
import hashlib
import requests

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

def update_db():
        """
        Update the database to the latest version from the GitHub repository.
        """
        try:
            # Step 1: Clone the repository or fetch the latest changes from the remote repository
            # For this example, we'll assume the repository URL is "https://github.com/username/repository.git"
            repo_url = "https://github.com/SteDiamant/StreamlitRegSystem.git"

            # You can use git or any version control tool to clone or fetch the latest changes.
            # For simplicity, we'll use the requests library to fetch the contents of the update file.
            update_url = f"{repo_url}/blob/master/users.db"  # Replace with the path to the update file.

            response = requests.get(update_url)
            if response.status_code == 200:
                update_script = response.text
            else:
                raise Exception(f"Failed to fetch update script. HTTP status code: {response.status_code}")

            # Step 2: Execute the update script or perform the necessary operations to update the database
            with sqlite3.connect("users.db") as conn:
                cursor = conn.cursor()
                
                # Execute the update script
                cursor.executescript(update_script)

                # Don't forget to commit the changes.
                conn.commit()

                print("Database updated successfully!")

        except Exception as e:
            print(f"Error updating the database: {e}")


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


class GitfCards():
    @staticmethod
    def create_giftcard_table():
        """
        Create the 'giftcards' table in the 'giftcards.db' SQLite database if it doesn't exist.

        The 'giftcards' table is used to store gift card data, including the description of the gift card,
        the source of the gift card (where it was obtained from), the amount of the gift card, and the date
        when the gift card data is added (current timestamp).

        The table schema:
            - Description (TEXT): Description or name of the gift card.
            - source (TEXT): Source or origin of the gift card.
            - amount (INTEGER): Amount of the gift card. It cannot be NULL.
            - date (TIMESTAMP DATETIME): Date and time when the gift card data is added to the table.
                                         It defaults to the current timestamp when not provided during insertion.

        Note:
        - The table will be created in the 'giftcards.db' database file. If the file doesn't exist, it will be created.
        - If the 'giftcards' table already exists, this function will not create a new table and will do nothing.

        Returns:
        None
        """
        conn = sqlite3.connect('giftcards.db')
        c = conn.cursor()
        # Create a table to store the gift card data
        c.execute('''CREATE TABLE IF NOT EXISTS giftcards
                    (Description TEXT NOT NULL, 
                    source TEXT NOT NULL,
                    amount INTEGER NOT NULL,
                    date TIMESTAMP DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        conn.close()
    @staticmethod
    def get_all_data():
        conn = sqlite3.connect('giftcards.db')
        c = conn.cursor()
        # Get all the data from the table
        c.execute('SELECT * FROM giftcards')
        data = c.fetchall()
        conn.close()
        return data
    @staticmethod 
    def insert_data(description, source, amount):
        conn = sqlite3.connect('giftcards.db')
        c = conn.cursor()
        # Insert the data into the table
        c.execute('INSERT INTO giftcards (Description, source, amount) VALUES (?, ?, ?)', (description, source, amount))
        conn.commit()
        conn.close()
    @staticmethod
    def update_data(description, source, amount, selected_date):
        """
        Update the gift card data in the database for the selected date

        Parameters:
            description (str): The description of the gift card.
            source (str): The source of the gift card.
            amount (int): The amount of the gift card.
            selected_date (str): The date when the gift card data is added to the table.
        """
        conn = sqlite3.connect('giftcards.db')
        c = conn.cursor()
        # Update the data in the table
        c.execute('UPDATE giftcards SET description=?, source=?, amount=? WHERE date=?', (description, source, amount, selected_date))
        conn.commit()
        conn.close()


class Invoice():
    @staticmethod
    def create_invoice_table():
        """
        Create the 'invoices' table in the 'invoices.db' SQLite database if it doesn't exist.
        """
        conn=sqlite3.connect('invoices.db')
        c=conn.cursor()
        # Create a table to store the invoice data
        c.execute('''CREATE TABLE IF NOT EXISTS invoices(name TEXT NOT NULL,
                  email TEXT NOT NULL,
                  amount INTEGER NOT NULL,
                  description TEXT NOT NULL,
                  date TIMESTAMP DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        conn.close()
    @staticmethod
    def get_all_data():
        conn = sqlite3.connect('invoices.db')
        c = conn.cursor()
        # Get all the data from the table
        c.execute('SELECT * FROM invoices')
        data = c.fetchall()
        conn.close()
        return data
    @staticmethod
    def insert_data(debiteur_name, debiteur_email,description,amount):
        conn = sqlite3.connect('invoices.db')
        c = conn.cursor()
        # Insert the data into the table
        c.execute('INSERT INTO invoices (name, email, description, amount) VALUES (?, ?, ?, ?)', (debiteur_name, debiteur_email, description, amount))
        conn.commit()
        conn.close()
    @staticmethod
    def update_data(debiteur_name, debiteur_email, amount, selected_date):
        """
        Update the invoice data in the database for the selected date

        Parameters:
            debiteur_name (str): The name of the debiteur.
            debiteur_email (str): The email of the debiteur.
            amount (int): The amount of the invoice.
            selected_date (str): The date when the invoice data is added to the table.
        """
        conn = sqlite3.connect('invoices.db')
        c = conn.cursor()
        # Update the data in the table
        c.execute('UPDATE invoices SET name=?, email=?, amount=? WHERE date=?', (debiteur_name, debiteur_email, amount, selected_date))
        conn.commit()
        conn.close()


class Card():
    @staticmethod
    def create_db():
        conn = sqlite3.connect('card_payments.db')
        c = conn.cursor()
        # Create a table to store the payment counts
        c.execute('''CREATE TABLE IF NOT EXISTS payments
                    (visa INTEGER, mastercard INTEGER, maestro INTEGER, vpay INTEGER,
                    total INTEGER, date TIMESTAMP DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_data():
        conn = sqlite3.connect('card_payments.db')
        c = conn.cursor()
        # Get all the data from the table
        c.execute('SELECT * FROM payments')
        data = c.fetchall()
        conn.close()
        return data

    @staticmethod
    def update_data(visa_count, mastercard_count, maestro_count, vpay_count, selected_date):
        """
        Update the card payment data in the database for the selected date.
        Args:
            visa_count (int): Count of Visa card payments.
            mastercard_count (int): Count of Mastercard payments.
            maestro_count (int): Count of Maestro card payments.
            vpay_count (int): Count of Vpay card payments.
            selected_date (str): The selected date in the form.

        Returns:
            bool: True if the data is successfully updated, False otherwise.
        """
        # Assuming you have the necessary database connection and table setup,
        # you can write the SQL query or ORM code here to update the data.
        # For example, using SQL and assuming the table name is 'card_payments':
        try:
            conn = sqlite3.connect('card_payments.db')  # Replace with your actual database connection function
            cursor = conn.cursor()
            update_query = "UPDATE payments SET visa=?, mastercard=?, maestro=?, vpay=?, total=? WHERE Date=?"
            total = visa_count + mastercard_count + maestro_count + vpay_count
            data_to_update = (visa_count, mastercard_count, maestro_count, vpay_count,total, selected_date)
            cursor.execute(update_query, data_to_update)
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error updating data: {e}")
            return False
        
    @staticmethod
    def insert_data(visa_count, mastercard_count, maestro_count, vpay_count):
        total = visa_count + mastercard_count + maestro_count + vpay_count
        conn = sqlite3.connect('card_payments.db')
        c = conn.cursor()
        # Insert the input values into the table, including the total count
        c.execute(f'INSERT INTO payments (visa, mastercard, maestro, vpay,total) VALUES (?, ?, ?, ?,?)',
                  (visa_count, mastercard_count, maestro_count, vpay_count,total))
        conn.commit()
        conn.close()