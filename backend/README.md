# SealMess - Backend

## Overview over roles, actions, and endpoints
* Roles: Customer, Provider, Owner (of the website, i.e. me)
* Actions: 
  * Customer:
    * can view, edit, and delete own account. 
    * can view providers and their menu items, and select menu items as their favorite ones.
    * can view the list of favorite menu items.
  * Provider:
    * can view, edit, and delete own account.
    * can view and edit own list of menu-items.
  * Owner:
    * can view statistics on customers, providers, and menu items: number of customers, number of providers, list of menu items sorted by how popular they are.
    * can view providers and their menu items.
    * can delete providers (e.g. in the case of violations)
* Endpoints:
  * GET
    * /customers/<int:customer_id>
    * /customers/<int:customer_id>/order
    * /providers
    * /providers/<int:provider_id>
    * /statistics
  * POST
    * /customers
    * /customers/<int:customer_id>/order
    * /providers
    * /providers/<int:provider_id>/menu
    * /search
  * PATCH
    * /customers/<int:customer_id>
    * /providers/<int:provider_id>
    * /providers/<int:provider_id>/menu/<int:menu_item_id>
  * DELETE
    * /customers/<int:customer_id>
    * /customers/<int:customer_id>/order/<int:menu_item_id>
    * /providers/<int:provider_id>
    * /providers/<int:provider_id>/menu/<int:menu_item_id>


## Getting started
### Installing Dependencies
#### Python 3.7
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

#### Virtual Enviornment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

#### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the /backend directory and running:

```bash
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.


## Database Setup
You have to create the database before running the server.

```bash
createdb sealmess
```

### Migrations
```bash
cd src/
export FLASK_APP=views/views.py
# flask db init
flask db migrate
flask db upgrade
# flask db downgrade
```

Alternatively, you can use the `migrate.py` script like this:
```bash
python3 manage.py db init --directory src/migrations/
python3 manage.py db upgrade --directory src/migrations/
python3 manage.py db migrate --directory src/migrations/
```

### Reset Databse
```bash
dropdb sealmess
createdb sealmess
flask db upgrade
```

## Running the server

Ensure first that you are working using your created virtual environment,
and that you are in the `backend` directory.

To run the server, execute:

```bash
python3 run.py
```

### Running the unittests
Ensure first that you are working using your created virtual environment,
and that you are in the `\backend` directory

Prepare the test database:
```bash
dropdb sealmess_test
createdb sealmess_test
psql sealmess_test < src/database/sealmess_test_db.psql
```

To run the unittests, execute:

```bash
python3 -m unittest src/tests/run_tests.py -v
```

# Customer
curl --request GET \
  --url https://sealmess.herokuapp.com/customers/1 \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik4wVXdOamxFTjBZMFJFSTFRa1ExT0RZeU56WXdOa1F3UkRZNU1VRkZNalJHTkVZME16RkZSQSJ9.eyJpc3MiOiJodHRwczovL2Rldi05cnFoMnRpYi5hdXRoMC5jb20vIiwic3ViIjoiT3daajVZUXFFN2tSUmhJNmY2S3RqbVdpMGdrMURwVGxAY2xpZW50cyIsImF1ZCI6InNlYWxtZXNzIiwiaWF0IjoxNTg3NjY1NzQyLCJleHAiOjE1ODc3NTIxNDIsImF6cCI6Ik93Wmo1WVFxRTdrUlJoSTZmNkt0am1XaTBnazFEcFRsIiwic2NvcGUiOiJwb3N0OmN1c3RvbWVyIGdldDpjdXN0b21lciBwYXRjaDpjdXN0b21lciBkZWxldGU6Y3VzdG9tZXIgcG9zdDpvcmRlciBnZXQ6b3JkZXIgZGVsZXRlOm9yZGVyIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOlsicG9zdDpjdXN0b21lciIsImdldDpjdXN0b21lciIsInBhdGNoOmN1c3RvbWVyIiwiZGVsZXRlOmN1c3RvbWVyIiwicG9zdDpvcmRlciIsImdldDpvcmRlciIsImRlbGV0ZTpvcmRlciJdfQ.grv-iwXrAmv6h-XBIN-3ZKyxUd_0nM-p2tnhJ2l1ZM2D1qoA2GQk2oHjzrs7qAHEnBPUq0GC6d89uuzRoMHigbioXumSxvE1ZqeK1-R78n8cvnUJem_Q0tlqoBOKCmljfDc6-1RUPoxen7RpTKr-VkO2iGQ1TEc-7JAQviliyPOffYMbQf8M9RseK5HdwbGdEV1LSwsro8f-vZ9IHte0ts5388MdhjbzTdCTMgEQiieeX8qEaJT5kiTykQL0ntaF4JEIoywTWazU0iT1e2lSnrWsbqgVIwRB4pvoheHhNpx4jFYbFi_UmKO63pvXB0mQAf02aVKRCbcpz_bbyL7R2w'

# Owner
  curl --request GET \
  --url https://sealmess.herokuapp.com/customers/1 \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik4wVXdOamxFTjBZMFJFSTFRa1ExT0RZeU56WXdOa1F3UkRZNU1VRkZNalJHTkVZME16RkZSQSJ9.eyJpc3MiOiJodHRwczovL2Rldi05cnFoMnRpYi5hdXRoMC5jb20vIiwic3ViIjoidXd6MHhVbWU0eXVaMHEyRmM5bW5FQkFoTkY1bjNIRHVAY2xpZW50cyIsImF1ZCI6InNlYWxtZXNzIiwiaWF0IjoxNTg3NjY2MTg0LCJleHAiOjE1ODc3NTI1ODQsImF6cCI6InV3ejB4VW1lNHl1WjBxMkZjOW1uRUJBaE5GNW4zSER1Iiwic2NvcGUiOiJkZWxldGU6cHJvdmlkZXIiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cHJvdmlkZXIiXX0.Up0gkdISLGANS-V5UrjclJ9JB9N8lqxsFlnI4wZsBYA-7StyAEkVYqf8HRaxypYTapKDCp9XpFGH-74cGcYv2AgrQCcoLNFv8FKGzLzJVxfpU-lkbBkFqWKGqLj63xtgJGHafEQVS6zpuvMxlXiS3Er75spEP1Cs-qP3TYxgljxfZBrui3YzOM_TqxzMVX6zd3EnG7LeUqipvZgS0udAPLYmUYKUFP1ng77SfotfBM4qfaX42bGHDFjWCevpxdrRKPEh1TeTESmY3wAJ3Mj81KTn8r92aA06K5uMJG-mbQPrWWUIJA6Xvjrl-ZDxw4bEceK8VffDBV-cSMJfIQCIPw'
  
  
  ### Development Setup

First, [install Flask](http://flask.pocoo.org/docs/1.0/installation/#install-flask) if you haven't already.

  ```
  $ cd ~
  $ sudo pip3 install Flask
  ```

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

2. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

3. Run the development server:
  ```
  $ export FLASK_APP=myapp
  $ export FLASK_ENV=development # enables debug mode
  $ python3 app.py
  ```

4. Navigate to Home page [http://localhost:5000](http://localhost:5000)
