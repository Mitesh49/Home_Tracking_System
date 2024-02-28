Home Maintenance Tracker

Overview
The Home Maintenance Tracker is a simple application designed to help users keep track of their home maintenance tasks. Users can log in, add tasks with specific frequencies (daily, weekly, monthly, quarterly, or annually), set reminders, and view their current tasks.

Features
- User Authentication: Users can sign up for a new account or log in with existing credentials.
- Task Management: Users can add new tasks, specifying their frequency and setting reminders.
- Reminder Notifications: Users receive reminders when tasks are due.
- Persistent Data Storage: Tasks are saved in a CSV file, and user credentials are stored in an Excel file.

Dependencies
- streamlit: Web application framework used for building the user interface.
- pandas: Library for data manipulation and analysis.
- time: Standard library for handling time-related functions.
- datetime: Standard library for working with dates and times.
- hashlib: Standard library for secure hashing algorithms.

Installation
1. Clone the repository:
   git clone https://github.com/your_username/home-maintenance-tracker.git
2. Install dependencies:
   pip install -r requirements.txt

Usage
1. Run the application:
   streamlit run app.py
2. If you're a new user, sign up for an account. Otherwise, log in with your credentials.
3. Add tasks by entering the task name, selecting its frequency, and setting a reminder.
4. View your current tasks and their details.
5. Receive reminders when tasks are due.

File Structure
- app.py: Main application file containing the Streamlit interface and functionality.
- tasks.csv: CSV file for storing tasks data.
- login.xlsx: Excel file for storing user credentials.
- requirements.txt: List of Python dependencies.

