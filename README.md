# InvoiceAPI

InvoiceAPI is a compact yet robust API built for efficiently managing invoices within smaller-scale projects. Its concise design offers essential endpoints for creating, retrieving, updating, and deleting invoices, along with seamless item integration.

## Table of Contents

#### [Features](#features)

#### [Installation](#installation)

#### [Usage](#usage)


#### [Contact](#contact)

## Features:

__Creation and Management of Invoices:__ Users can easily create new invoices, specifying invoice details such as description, list of items, as well as sender and receiver information.

__Payment Terms Selection:__ When creating an invoice, users can choose payment terms from a provided list of options (1 Day, 7 Days, 14 Days, 30 Days), providing flexibility in managing cash flows.

__Automatic Serial Number Generation:__ Invoice serial numbers are automatically generated using a unique algorithm, ensuring uniqueness and ease of tracking.

__Automatic Calculation of Invoice Amount:__ When adding items to an invoice, the application automatically calculates the total invoice amount based on item prices and quantities.

__Setting Payment Due Date:__ The application automatically sets the payment due date based on the selected payment terms, helping users clearly see payment deadlines.

__Invoice Status:__ Each invoice has a status, which can be "pending", "paid", or "draft" providing transparency in invoice tracking.

### Advantages:

__Efficient Invoice Management:__ Users can easily track invoice statuses update items in it and manage payment terms.
__Process Automation:__ Automatic calculation of invoice amounts and setting payment due dates reduce the time spent on manual calculations and setting payment deadlines.
__Security and Convenience:__ The application ensures secure storage of user data and provides a convenient interface for accessing invoice information.

### Technology Stack:

__Django:__ The Django web framework is used for developing the server-side of the application, providing a powerful and secure tool for working with databases and handling requests.

__Python:__ Python programming language is used for writing the business logic of the application, including serial number generation, invoice amount calculations, and payment date setting.

## Installation (!!!Commands may vary for your OS!!!)

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

