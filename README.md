# Pet Adoption & Rescue Management System

This is a Django-based web application for managing pet adoption and rescue reports. It helps reunite lost pets with their owners and facilitates pet adoption through a centralized platform.

## Features

### User Features
* **User Authentication:** Secure registration, login, and logout.
* **Report Pets:** Users can report "Lost Pets" and "Found Pets" with detailed descriptions, locations, and photos.
* **Advanced Search:** Search for pets using filters for pet type, breed, color, and date ranges. Includes sorting options (Newest, Oldest, Location).
* **Pet Details:** Detailed profile pages for each pet, displaying full information and the reporter's contact details (for logged-in users).
* **User Dashboard:** A "My Dashboard" section for users to view, edit, and delete their own pending reports.
* **Contact Us:** A contact form for users to send inquiries to the administration.

### Admin Features
* **Custom Admin Dashboard:** A dedicated dashboard for superusers to review, accept, or reject pet reports.
* **Notification System:** Real-time notification badges and a dropdown menu in the navigation bar alerting admins to new pending requests.
* **Request Management:** Efficient workflow to manage "Lost" and "Found" reports.

## Tech Stack
* **Backend:** Django 5.0 (Python)
* **Database:** MySQL
* **Frontend:** HTML5, CSS3, Bootstrap 5 (for responsive design and styling)
* **Icons:** Bootstrap Icons

## Setup and Installation

These instructions will get you a copy of the project up and running on your local machine.

### 1. Prerequisites
* Python 3.10+
* MySQL Server
* Git

### 2. Installation

1.  **Clone the repository:**
    ```sh
    git clone <your-repository-url>
    cd petadopt
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```sh
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up the Database:**
    * Open your MySQL client (e.g., MySQL Workbench).
    * Create a new database (schema) named `petadopt_db`.

5.  **Configure Environment:**
    * Open `petadopt/settings.py`.
    * Find the `DATABASES` section and update the `PASSWORD` with your MySQL root password.

6.  **Run Migrations:**
    This will create the necessary tables in your database.
    ```sh
    python manage.py migrate
    ```

7.  **Create a Superuser:**
    Create an admin account to access the dashboard.
    ```sh
    python manage.py createsuperuser
    ```

8.  **Run the Server:**
    ```sh
    python manage.py runserver
    ```

### 3. Access the Application
* **Home Page:** `http://127.0.0.1:8000/`
* **Admin Dashboard:** `http://127.0.0.1:8000/admin-dashboard/` (Requires superuser login)

## License
This project is open-source and available for educational purposes.