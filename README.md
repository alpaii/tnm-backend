# Django Project Setup Guide

Follow the steps below to set up a Django project:

## Step 1: Create a Python Virtual Environment

To isolate your project dependencies, create a Python virtual environment.

1. Open a terminal and navigate to your desired project directory.
2. Run the following command to create a virtual environment:

   ```bash
   python -m venv venv
   ```

   Replace `venv` with your preferred virtual environment name, if needed.

3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Once activated, your terminal prompt will change to indicate the active environment.

## Step 2: Install Django

With the virtual environment activated, install Django using pip:

```bash
pip install django
```

## Step 3: Create a Django Project

1. Create a new Django project by running:

   ```bash
   django-admin startproject project_name
   ```

   Replace `project_name` with the desired name for your project.

2. Navigate into the newly created project directory:

   ```bash
   cd project_name
   ```

3. Verify the setup by running the development server:

   ```bash
   python manage.py runserver
   ```

4. Open your browser and go to `http://127.0.0.1:8000/`. You should see the default Django welcome page.

## Notes

- Always remember to activate your virtual environment before working on the project.
- To deactivate the virtual environment, run:

  ```bash
  deactivate
  ```

Congratulations! You have successfully set up a Django project.
