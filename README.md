# InvoiceAPI

InvoiceAPI is a compact yet robust API built for efficiently managing invoices within smaller-scale projects. Its concise design offers essential endpoints for creating, retrieving, updating, and deleting invoices, along with seamless item integration.

## Table of Contents

#### [Installation](#installation)

#### [Usage](#usage)

#### [Contact](#contact)

## Installation 

### !!!Commands may vary for your OS!!!

__1. Clone the repository:__

```
git clone https://github.com/pro100sergosha/InvoiceAPI.git
```
__2. Navigate to the project directory:__

```
cd InvoiceAPI
```

__3. Create virtual environment:__
```
python -m venv venv
```

__4. Activate your virtual enviroment:__
```
venv\Scripts\activate
```
__5. Install the dependencies:__

```
pip install -r requirements.txt
```

__6. Set up environment variables by creating a .env file in the root directory. Use .env.example as a template:__
```
code .env
```
__7. Apply the database migrations to set up the database schema:__
```
python manage.py migrate
```
__8. Start the application__:
```
python manage.py runserver
```
## Usage

After the installation, the API can be accessed at http://localhost:8000. You can use tools like [Postman](https://www.postman.com/downloads/) or other similar applications to interact with the endpoints.

__For detailed documentation of all endpoints, please refer to the API Documentation below.__

[Swagger Documentation](https://app.swaggerhub.com/apis-docs/SergoAzizbekyan/invoice-api/v1)


## Contact
For any questions or suggestions, please contact prizrakgames21@mail.ru.

