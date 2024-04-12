# with raanom value upate



# import sqlite3
# import hashlib

# # Connect to the SQLite database (or create it if it doesn't exist)
# conn = sqlite3.connect('user_database.db')
# c = conn.cursor()

# # Create users table if not exists
# c.execute('''CREATE TABLE IF NOT EXISTS users (
#                 id INTEGER PRIMARY KEY,
#                 username TEXT UNIQUE,
#                 password TEXT,
#                 random_value INTEGER
#             )''')
# conn.commit()

# def signup():
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if not username or not password:
#         print("Username and password cannot be empty. Please try again.")
#         return

#     random_value = None  # Set random value to None during signup

#     # Hash the password before storing it
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()

#     # Insert user data into the database
#     c.execute("INSERT INTO users (username, password, random_value) VALUES (?, ?, ?)",
#               (username, hashed_password, random_value))
#     conn.commit()
#     print("Signup successful!")

# def login():
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     # Hash the password for comparison
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()

#     # Check if the username and hashed password match what's in the database
#     c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
#     user = c.fetchone()
#     if user:
#         print("Login successful!")
#         return user[0], user[3]  # Return the user ID and the random value associated with the user
#     else:
#         print("Login failed. Invalid username or password.")
#         return None, None

# def update_random_value(user_id, random_value):
#     c.execute("UPDATE users SET random_value=? WHERE id=?", (random_value, user_id))
#     conn.commit()

# def main():
#     while True:
#         print("\n1. Signup")
#         print("2. Login")
#         print("3. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             signup()
#         elif choice == '2':
#             user_id, current_random_value = login()
#             if user_id is not None:
#                 new_random_value = int(input("Enter a new random value: "))
#                 update_random_value(user_id, new_random_value)
#                 print("Random value updated successfully!")
#         elif choice == '3':
#             break
#         else:
#             print("Invalid choice. Please try again.")

#     conn.close()

# if __name__ == "__main__":
#     main()



# with raanom value update and insert new row


# import sqlite3
# import hashlib

# # Connect to the SQLite database (or create it if it doesn't exist)
# conn = sqlite3.connect('user_database.db')
# c = conn.cursor()

# # Create users table if not exists
# c.execute('''CREATE TABLE IF NOT EXISTS users (
#                 id INTEGER PRIMARY KEY,
#                 username TEXT,
#                 password TEXT,
#                 random_value INTEGER
#             )''')
# conn.commit()

# def signup():
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if not username or not password:
#         print("Username and password cannot be empty. Please try again.")
#         return

#     random_value = None  # Set random value to None during signup

#     # Hash the password before storing it
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()

#     # Insert user data into the database
#     c.execute("INSERT INTO users (username, password, random_value) VALUES (?, ?, ?)",
#               (username, hashed_password, random_value))
#     conn.commit()
#     print("Signup successful!")

# def login():
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     # Hash the password for2 comparison
#     hashed_password = hashlib.sha256(password.encode()).hexdigest()

#     # Check if the username and hashed password match what's in the database
#     c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
#     user = c.fetchone()
#     if user:
#         print("Login successful!")
#         return user[0], user[3]  # Return the user ID and the random value associated with the user
#     else:
#         print("Login failed. Invalid username or password.")
#         return None, None

# def update_random_value(user_id, random_value):
#     # Check if the user already has a random value
#     c.execute("SELECT * FROM users WHERE id=?", (user_id,))
#     user = c.fetchone()
#     if user[3] is None:
#         # If the user doesn't have a random value, update the existing row
#         c.execute("UPDATE users SET random_value=? WHERE id=?", (random_value, user_id))
#     else:
#         # If the user already has a random value, insert a new row
        # c.execute("INSERT INTO users (username, password, random_value) VALUES (?, ?, ?)",
        #           (user[1], user[2], random_value))
#     conn.commit()

# def main():
#     while True:
#         print("\n1. Signup")
#         print("2. Login")
#         print("3. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             signup()
#         elif choice == '2':
#             user_id, current_random_value = login()
#             if user_id is not None:
#                 new_random_value = int(input("Enter a new random value: "))
#                 update_random_value(user_id, new_random_value)
#                 print("Random value updated successfully!")
#         elif choice == '3':
#             break
#         else:
#             print("Invalid choice. Please try again.")

#     conn.close()

# if __name__ == "__main__":
#     main()





# with userid columnn





import sqlite3
import hashlib
import time

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('user_database.db')
c = conn.cursor()

# Create users table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                user_id TEXT,
                username TEXT,
                password TEXT,
                random_value INTEGER
            )''')
conn.commit()

user_id_counter = 0  # Unique counter for generating user IDs

def generate_user_id(username, password):
    global user_id_counter  # Access the global user_id_counter variable
    # Combine username, password, and a unique integer value (timestamp)
    combined = username + password + str(int(time.time())) + str(user_id_counter)
    # Hash the combined string to generate a unique user ID
    user_id = int(hashlib.sha256(combined.encode()).hexdigest(), 16) % (10 ** 10)  # Limit to 10 digits
    user_id_counter += 1  # Increment the counter for the next user
    return user_id



def signup():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not username or not password:
        print("Username and password cannot be empty. Please try again.")
        return

    # Check if the username already exists
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    if c.fetchone():
        print("Username already exists. Please choose a different username.")
        return

    random_value = None  # Set random value to None during signup

    # Generate user ID
    user_id = generate_user_id(username, password)

    # Hash the password before storing it
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Insert user data into the database
    c.execute("INSERT INTO users (user_id, username, password, random_value) VALUES (?, ?, ?, ?)",
              (user_id, username, hashed_password, random_value))
    conn.commit()
    print("Signup successful!")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hash the password for comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the username and hashed password match what's in the database
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    user = c.fetchone()
    if user:
        print("Login successful!")
        return user[1], user[4]  # Return the user_id and the random value associated with the user
    else:
        print("Login failed. Invalid username or password.")
        return None, None

def update_random_value(user_id, random_value):
    # Check if the user already has a random value
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = c.fetchone()
    if user[4] is None:
        # If the user doesn't have a random value, update the existing row
        c.execute("UPDATE users SET random_value=? WHERE user_id=?", (random_value, user_id))
    else:
        # If the user already has a random value, insert a new row
        c.execute("INSERT INTO users (user_id, username, password, random_value) VALUES (?, ?, ?, ?)",
                  (user_id, user[2], user[3], random_value))
    conn.commit()

def main():
    while True:
        print("\n1. Signup")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            signup()
        elif choice == '2':
            user_id, current_random_value = login()
            if user_id is not None:
                new_random_value = int(input("Enter a new random value: "))
                update_random_value(user_id, new_random_value)
                print("Random value updated successfully!")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()











# with questions and answers column




import sqlite3
import hashlib
import time
from iso_qa_export import answer_question_from_pdf

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('user_database.db')
c = conn.cursor()

# Create users table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                user_id TEXT,
                username TEXT,
                password TEXT,
                question TEXT,
                answer TEXT
            )''')
conn.commit()

user_id_counter = 0  # Unique counter for generating user IDs

def generate_user_id(username, password):
    global user_id_counter  # Access the global user_id_counter variable
    # Combine username, password, and a unique integer value (timestamp)
    combined = username + password + str(int(time.time())) + str(user_id_counter)
    # Hash the combined string to generate a unique user ID
    user_id = int(hashlib.sha256(combined.encode()).hexdigest(), 16) % (10 ** 10)  # Limit to 10 digits
    user_id_counter += 1  # Increment the counter for the next user
    return user_id

def signup():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not username or not password:
        print("Username and password cannot be empty. Please try again.")
        return

    # Check if the username already exists
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    if c.fetchone():
        print("Username already exists. Please choose a different username.")
        return

    # Generate user ID
    user_id = generate_user_id(username, password)

    # Hash the password before storing it
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Insert user data into the database
    c.execute("INSERT INTO users (user_id, username, password, question, answer) VALUES (?, ?, ?, ?, ?)",
              (user_id, username, hashed_password, None, None))
    conn.commit()
    print("Signup successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hash the password for comparison
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the username and hashed password match what's in the database
    c.execute("SELECT user_id, question, answer FROM users WHERE username=? AND password=?", (username, hashed_password))
    user = c.fetchone()
    if user:
        print("Login successful!")
        return user
    else:
        print("Login failed. Invalid username or password.")
        return None

def add_question_and_answer(user_id, question, answer):
    # Add a new row for the question and answer for the user
    c.execute("INSERT INTO users (user_id, username, password, question, answer) VALUES (?, ?, ?, ?, ?)",
              (user_id, "", "", question, answer))
    conn.commit()


def main():
    while True:
        print("\n1. Signup")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            signup()
        elif choice == '2':
            user = login()
            if user:
                question = input("Enter your question: ")
                # Here you can call the function answer_question_from_pdf() passing the file and the question
                answer = answer_question_from_pdf("/Users/macbook/Desktop/multiusrdb/docs/ISO+13485-2016.pdf", question)
                if answer:
                    add_question_and_answer(user[0], question, answer)
                    print("Question and answer added successfully!")
                else:
                    print("Failed to retrieve answer.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()