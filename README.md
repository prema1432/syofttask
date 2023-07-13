# Syoft Task

This repository contains the solution for the backend task. It implements three API endpoints for user registration, login, and product CRUD operations. The project is built using Django and Django Rest Framework.

## Task Description

The task involves developing the following API endpoints:

1. **Register**: Create a POST request to register a new user with the required fields.

2. **Login**: Create a POST request to authenticate a user and obtain an access token.

3. **Product CRUD**: Implement the CRUD operations (Create, Read, Update, Delete) for managing products. Access to these operations is restricted based on user roles and token authentication.
- All the CRUD operations should require a token in the request header. If no token is provided, return a 400 status code with a message indicating that the token was not provided.

- Product Creation can only be accessed with an admin token.
- Product Get can be accessed with an admin or manager token.
- Product Update can be accessed with an admin or manager token.
- Product Delete can only be accessed with an admin token.
- Staff members will not have any CRUD rights.


## Installation and Usage

1. Clone the repository:

   ```shell
   git clone https://github.com/prema1432/syofttask

2. Create a virtual environment for the project: python3 -m venv env

3. Activate the virtual environment:
On Linux/Mac: source env/bin/activate
On Windows: .\env\Scripts\activate

4. Install the project dependencies: pip install -r requirements.txt

5.Set up the database (PostgreSQL):
Create a new PostgreSQL database.
Update the database settings in the settings.py file of the Django project

6. Apply the database migrations: **python manage.py makemigrations and  python manage.py migrate**

7. Start the Django development server: **python manage.py runserver**

## Swagger Documentation

Swagger is a powerful tool for documenting and testing APIs. It provides a user-friendly interface where you can explore the available endpoints, view request/response examples, and test the API directly.

To access the Swagger documentation for this project, follow these steps:

1. Start the Django development server.
2. Open your web browser and go to the following URL: `http://127.0.0.1:8000/api/schema/swagger-ui/`

You will see the Swagger documentation page with the available endpoints and their descriptions. You can click on each endpoint to expand it and view the request/response details. Use the provided "Try it out" button to send requests and see the responses directly within the Swagger interface.

## API Endpoints
Register: POST /api/register/
Login: POST /api/login/
Product List: GET /api/product/list/
Product Detail: GET /api/product/{id}/
Product Create: POST /api/product/create/
Product Update: PUT /api/product/{id}/
Product Delete: DELETE /api/product/{id}/
