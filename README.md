# openmrs-backend

Project for practice

## Install Environment

1. **Create a virtual environment** (if you don't have one already):

   - For `venv`:
     ```bash
     python -m venv venv
     ```
   - For `virtualenv`:
     ```bash
     virtualenv venv
     ```

2. **Activate the virtual environment**:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Set Up the Databasement

1. **Apply database migrations** :

   ```bash
   python manage.py migrate
   ```

## Run the App

1. **Start the development server**: After setting up your environment and applying migrations, you can start the Django development server with:

   ```bash
   python manage.py runserver
   ```

Access the app: Open your browser and go to http://127.0.0.1:8000/ to view the app.

## Optional: Create a Superuser (Admin Account)

If you want to access the Django admin interface, you need to create a superuser (admin) account:

1. Run the following command to create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

2. Follow the prompts to set up your admin user ( email, and password).

3. Once the superuser is created, you can log in to the admin interface at:
   http://127.0.0.1:8000/admin/
