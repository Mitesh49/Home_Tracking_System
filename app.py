import streamlit as st
import pandas as pd
import time
from datetime import datetime, timedelta
import hashlib

# Function to load or create maintenance tasks DataFrame
@st.cache(allow_output_mutation=True)
def load_tasks():
    try:
        tasks = pd.read_csv('tasks.csv')
    except FileNotFoundError:
        tasks = pd.DataFrame({'Task': [], 'Frequency': [], 'Reminder': []})
    return tasks


# Function to save tasks DataFrame
def save_tasks(tasks):
    tasks.to_csv('tasks.csv', index=False)

# Function to add a new task
def add_task(tasks, task, frequency, reminder):
    new_task = pd.DataFrame({'Task': [task], 'Frequency': [frequency], 'Reminder': [reminder]})
    tasks = pd.concat([tasks, new_task], ignore_index=True)
    save_tasks(tasks)
    return tasks

# Function to display reminder message when the timer ends
def reminder_message(task):
    st.error(f"Time's up! Remember to complete the task: {task}")

# Function to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to authenticate user
def authenticate(username, password):
    try:
        users_df = pd.read_excel('login.xlsx')
    except FileNotFoundError:
        return False

    hashed_password = hash_password(password)
    if ((users_df['Username'] == username) & (users_df['Password'] == hashed_password)).any():
        return True
    return False

# Function to sign up user
def signup(username, password):
    try:
        users_df = pd.read_excel('login.xlsx')
    except FileNotFoundError:
        users_df = pd.DataFrame({'Username': [], 'Password': []})

    hashed_password = hash_password(password)
    new_user = pd.DataFrame({'Username': [username], 'Password': [hashed_password]})
    users_df = pd.concat([users_df, new_user], ignore_index=True)
    users_df.to_excel('login.xlsx', index=False)

# Main function
def main():
    st.title('Home Maintenance Tracker')

    # Authentication
    session_state = st.session_state
    if 'logged_in' not in session_state:
        session_state.logged_in = False

    if not session_state.logged_in:
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if authenticate(username, password):
                session_state.logged_in = True
            else:
                st.error("Invalid username or password")

        st.subheader("Sign Up if you are new")
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        if st.button("Sign Up"):
            signup(new_username, new_password)
            st.success("Signup successful, you can now login.")

    else:
        # Load tasks DataFrame
        tasks = load_tasks()

        st.header('Add New Task')

        new_task = st.text_input('Task')
        frequency = st.selectbox('Frequency', ['Daily', 'Weekly', 'Monthly', 'Quarterly', 'Annually'])
        reminder = st.slider('Set Reminder (minutes before due)', min_value=1, max_value=1440, step=1, value=30)

        if st.button('Add Task'):
            tasks = add_task(tasks, new_task, frequency, reminder)
            due_time = datetime.now() + timedelta(minutes=reminder)
            st.write(f"Task '{new_task}' due at: {due_time.strftime('%Y-%m-%d %H:%M:%S')}")

            with st.spinner("Timer is running..."):
                time.sleep(reminder * 60)  # Convert minutes to seconds
                reminder_message(new_task)

        st.header('Current Tasks')
        if tasks.empty:
            st.write('No tasks added yet.')
        else:
            # Display tasks without 'Last Completed' column
            tasks_display = tasks.drop(columns=['Last Completed'])
            st.write(tasks_display)

        st.write('© 2024 Home Maintenance Tracker')

if _name_ == '_main_':
    main()