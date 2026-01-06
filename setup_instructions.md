# Employee Management System - Setup Instructions

## Prerequisites
- Python 3.8+ installed
- pip (Python package manager)

## Installation Steps

1.  **Navigate to the project directory:**
    ```bash
    cd c:/Users/cselab4/Downloads/Employee_management
    ```

2.  **Install Django:**
    ```bash
    pip install django
    ```

3.  **Run Migrations (Database Setup):**
    ```bash
    python manage.py makemigrations employees
    python manage.py migrate
    ```

4.  **Create Superuser (Admin):**
    A script is provided to automatically create a superuser with username `admin` and password `admin`.
    ```bash
    python create_superuser.py
    ```
    *Alternatively, you can run `python manage.py createsuperuser` and follow the prompts.*

5.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```

## Usage

1.  Open your web browser and go to `http://127.0.0.1:8000/`.
2.  You will be redirected to the login page.
3.  Login with:
    - **Username:** `admin`
    - **Password:** `admin`
4.  **Dashboard:** View total employees count.
5.  **Add Employee:** Click "Add Employee" in navbar or dashboard to create a new record.
6.  **Employees List:** View all employees, search by name or department.
7.  **Edit/Delete:** use the buttons in the employee list.
8.  **Logout:** Click Logout in the navbar.

## Project Structure
- `employee_system/`: Main project configuration (settings, urls).
- `employees/`: Employee management app (models, views, forms).
- `templates/`: HTML templates (Bootstrap 5).
- `db.sqlite3`: Local database file.
- `create_superuser.py`: Automation script.
