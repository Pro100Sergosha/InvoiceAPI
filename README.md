# InvoiceAPI

InvoiceAPI is a robust and scalable API designed to manage invoices efficiently. This API provides endpoints for creating, retrieving, updating, and deleting invoices, making it easy to integrate with other systems and applications.

## Table of Contents

#### [Features](#features)

#### [Installation](#installation)

#### [Usage](#usage)

#### [Endpoints](Endpoints)

#### [Configuration](#configuration)

#### [Contact](#contact)


## Features

Create, read, update, and delete invoices

Search and filter invoices by various criteria

Comprehensive error handling and validation

Support for multiple data formats (JSON, XML)

Easy integration with external systems

Installation
Prerequisites
Python (>= 3.8)
PostgreSQL (>= 12.x)
Steps
Clone the repository:


git clone https://github.com/yourusername/InvoiceAPI.git

Navigate to the project directory:

cd InvoiceAPI

Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac OS
    ```
    ```cmd
    python -m venv venv
    venv\Scripts\activate  # For Windows
    ```
Install the dependencies:

pip install -r requirements.txt
Set up environment variables by creating a .env file in the root directory. Use .env.example as a template:

cp .env.example .env
Update the .env file with your PostgreSQL connection details:

env
```
SECRET_KEY=your_secret_key
DATABASE_NAME=invoiceapi
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```
Apply the database migrations to set up the database schema:
```
python manage.py migrate
```
Create a superuser to access the Django admin interface:
```
python manage.py createsuperuser
```
__Start the application__:
```
python manage.py runserver
```
__Usage__
After the installation, the API can be accessed at http://localhost:8000. You can use tools like Postman or curl to interact with the endpoints.

## Endpoints
Here are some of the main endpoints available in InvoiceAPI:

Invoices
GET /api/invoices/: Retrieve all invoices
GET /api/invoices/:id/: Retrieve a specific invoice by ID
POST /api/invoices/: Create a new invoice
PUT /api/invoices/:id/: Update an existing invoice by ID
DELETE /api/invoices/:id/: Delete an invoice by ID
For detailed documentation of all endpoints, please refer to the API Documentation.
https://app.swaggerhub.com/apis-docs/SergoAzizbekyan/invoice-api/v1

Configuration
The application can be configured using environment variables. Below are the key configuration options:

SECRET_KEY: The secret key for Django
DATABASE_NAME: The name of the PostgreSQL database
DATABASE_USER: The user for the PostgreSQL database
DATABASE_PASSWORD: The password for the PostgreSQL database user
DATABASE_HOST: The host of the PostgreSQL database (e.g., localhost)
DATABASE_PORT: The port of the PostgreSQL database (default: 5432)


Contact
For any questions or suggestions, please contact prizrakgames21@mail.ru.

