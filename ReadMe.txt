## City Bikes - Online Bike Marketplace

City Bikes is a Django-powered online platform that facilitates buying and selling bikes. It utilizes Django Rest Framework for API development and integrates JSON Web Tokens (JWT) for security and authentication.


## Features

- Users can list their bikes for sale.
- Buyers can browse and search for available bikes.
- Secure authentication using JWT.
- RESTful API for seamless integration with front-end applications.

## Installation
install dependencies using pip install -r requirements.txt

Apply database migrations:

python manage.py migrate

Create a superuser account:

python manage.py createsuperuser

Run the development server:

python manage.py runserver

Your City Bikes app should now be running at http://localhost:8000/.

## Prerequisites

- Python (version 3.6 or later)
- Django (version 3.2)
- Django Rest Framework (version 3.12)
- Other dependencies...

#Usage
Access the Django admin interface at http://localhost:8000/admin/ to manage users, listings, and other data.
Use API endpoints for programmatic access to data (see API Endpoints).
Integrate City Bikes API with your front-end application.

#Configuration
Adjust configuration settings in settings.py as needed. Customize models, serializers, and views to match your project requirements.
