# - Running Application without docker

To run the application follow the `README.md` file inside each `backend` and `frontend` folder

# - Run Application Using Docker

1. In both `backend` and `frontend` folder make sure to copy `.env.example` to `.env` and update with correct values so that the env variables can be injected to the docker container for execution

2. Run `docker compose -f dockercompose.yml up --build` in the project root folder where `dockercompose.yml` file exists, it will start the following:

- frontend server accessible at port `5173`
- backend server accessible at port `8000`

### Load mock data into the backend server running in docker containers:

1. Fetch the id for the docker container running for the backend using:<br>
    `docker ps`

2. Open the shell inside the docker container for the backend using:<br>
    `docker exec -it <container_id> sh`

3. Run the following command to clear the existing data and populate mock data using:<br>
    `python manage.py populate_mock_data --clear`

4. To create a default admin user execute following:<br>
    `python manage.py createsuperuser`<br>
    then pass the required values and once done, you can log in as the superuser from `https://localhost:8000/admin`

# Important Endpoints:


- frontend server                   : `http://localhost:5173`
- backend server                    : `http://localhost:8000`
- Swagger docs                      : `http://localhost:8000/swagger`
- Django Admin                      : `http://localhost:8000/admin`
- Backend Health check endpoint     : `http://localhost:8000/`