## Backend Project Setup

1. Create virtual environment
```python -m venv v_env```

2. Activate virtual environment using ```v_env/scripts/activate```

3. Install the dependencies for the applicaiton ```pip install -r requirements.txt```

4. Copy the `.env.example` and rename it to `.env` and update the env variables with actual values

5. Apply migrations using `python manage.py migrate` to create required tables and database

6. If you want to load mock data into the database using command `python manage.py populate_mock_data` and if you want to clean the existing data while populating mock data then use `python manage.py populate_mock_data --clear`

7. To create a default admin user execute following:<br>
    `python manage.py createsuperuser`<br>
    then pass the required values and once done, you can log in as the superuser from `https://localhost:8000/admin`

8. Finally Django server can be started using `python manage.py runserver` and it will be accessible at `http://localhost:8000`