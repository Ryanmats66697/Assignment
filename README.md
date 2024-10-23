# Rule Engine Application & Weather App

This is a rule engine application built using Django, allowing you to create, modify, and evaluate rules based on user profile data such as age, income, and department. The application comes with pre-configured virtual environment files and database, making setup easier.

## Features
- Add and manage rules.
- Add and manage user profiles.
- Evaluate rules based on user data.

## Prerequisites

Make sure you have **Python 3.8** or higher installed on your machine.

## Setup Instructions

1. **Clone the Repository**

   Clone the project repository from GitHub using the following command:

   ```bash
   git clone https://github.com/Ryanmats66697/Assignment.git
   cd Assignment

   
2. **Activate the Pre-configured Virtual Environment**

The repository includes a pre-configured virtual environment (venv), so you don’t need to install the dependencies manually. To activate the virtual environment, use the following commands:

On Linux/Mac:

  bash
  Copy code
  source venv/bin/activate


3. **Navigate to the manage.py Folder**

cd project/rule_engine


4.**Start the Development Server**

After activating the virtual environment and setting up the database, start the Django development server using:

  bash
  Copy code
  python manage.py runserver


5.**Access the Application**

Once the server is running, you can access the application via your web browser. The API and admin interface are available at the following URLs:

API Base URL: http://127.0.0.1:8000/api/
Django Admin: http://127.0.0.1:8000/admin/ (log in with your superuser credentials)
Weather: http://127.0.0.1:8000/weather/
