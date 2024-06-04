# Preparing and Running the Flask API for the Register

There are two ways to prepare and run the API: using Docker or directly with Flask.

## Requirements for Docker

Docker
Git
## Instructions to Build and Run the Application with Docker

1.Clone the Repository:
```
git clone https://github.com/PolMuri/api.git
cd api
```

2.Build the Docker Image:
````
docker image build -t register_docker1 .
````

3.Run the Container:
````
docker run -p 80:5000 register_docker1
````

Alternatively, if you want to control exactly where these persistent data are stored on your host system, you should use the -v option when running the container. This allows you to mount a specific directory from your host system instead of the anonymous volume Docker creates by default.
````
docker run -p 80:5000 -v /path/to/local/folder:/data register_docker1
````
Note: Replace ``/path/to/local/folder`` with the actual path on your system where you want to store the persistent data.

4.Verify the Application is Running:

Open a browser and go to ``http://localhost:80``. You should see the application running.

5.Make a Test Request with Curl:
````
curl -d '{"email":"youremail@example.com"}' -H "Content-Type: application/json" -X POST http://localhost/api/register/
````

## Initial Configuration to Run the Application with Flask
1.Clone the Repository:
````
git clone <repository_url.git> cd <directory_name>
````

2.Configure the Database:

You can use a script or specific tools to initialize or configure the database as needed.

## Run the API:
````
python app.py
````
The API will be available by default at ``http://127.0.0.1:5000/``.

## Testing the API

1.Register a User:

-Allows you to register new users by providing their email address.

-Generates a unique authentication token for each registered user.

-Stores user information, including their email and token, in a database file db.json.
````
curl -X POST -H "Content-Type: application/json" -d '{"email": "example@email.com"}' http://127.0.0.1:5000/api/register/
````
This will return a token and register the user in the database.

You can find the registered user in the db.json file, which is automatically created if it does not already exist and acts as the database.

2.Initialize Password:

-Allows initializing passwords for existing users.

-Finds a user by their token and saves a secure hash of the provided password in db.json.
````
curl -X POST -H "Content-Type: application/json" -d '{"token": "token", "password": "password"}' http://127.0.0.1:5000/api/init/
````
This will initialize the password for the user associated with the provided token.

3.Login:

-Facilitates the login process for registered users.

-Generates an authorization token (Bearer token) for the provided user, allowing access to protected resources.
````
curl -X POST -H "Content-Type: application/json" -d '{"email": "example@email.com", "password": "password"}' http://127.0.0.1:5000/api/login
````
This will log in the user with the provided email and password.

4.Verify Token:

-Allows verifying a JWT authorization token and displays its content (payload).

-Requires the public key associated with the private key used during the login process.
````
curl -X POST -H "Content-Type: application/json" -d '{"token": "token"}' http://127.0.0.1:5000/api/verify
````
This will verify the provided token and display the payload of the JWT if it is valid.

## Project Structure

-app.py: Main file that defines the Flask application and routes.
-register.py: Registration logic with functions such as generate_token, is_valid_email, and add_user.
-db.py: Database-related functions such as load_data, save_data, is_valid_email, and add_user.
-init.py: Functions related to password initialization such as initialize_password.
-login.py: Functions related to login such as login and validate_password.
-verify.py: Contains the function to verify a JWT token verify_token.

##Note

Make sure to have Python and the required tools installed in the environment before running the API.


