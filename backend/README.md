# sealmess backend

## Table of Contents


## Live Deployment on Heroku
The app is hosted live on Heroku: https://sealmess.herokuapp.com/

## Development Setup
### Python 3.7
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

### Virtual Enviornment
General information on how to set up a virtual envirinment can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).
```bash
$ python3 -m venv env
$ source env/bin/activate
```

### Install Dependencies
Once you have your virtual environment setup and running, install the dependencies:
```bash
$ pip3 install -r requirements.txt
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.


## Database Setup
You have to create the database before running the server.

```bash
$ createdb sealmess
```

Also make sure to load the necessary environment variables
```bash
$ source setup.sh
```

### Migrations
```bash
$ cd src/
$ export FLASK_APP=views/views.py
# flask db init
$ flask db migrate
$ flask db upgrade
# flask db downgrade
```

Alternatively, you can use the `migrate.py` script like this:
```bash
$ python3 manage.py db init --directory src/migrations/
$ python3 manage.py db upgrade --directory src/migrations/
$ python3 manage.py db migrate --directory src/migrations/
```

### Reset Database
```bash
$ dropdb sealmess
$ createdb sealmess
$ flask db upgrade
```

## Running the server
Ensure first that you are working using your created virtual environment,
and that you are in the `backend` directory.

To run the server, execute:
```bash
$ source env/bin/activate
$ source setup.sh
$ python3 run.py
```

Navigate to Home page [http://localhost:5000](http://localhost:5000)

## Testing
Ensure that you are working using your created virtual environment. If not, run:
```bash
$ source env/bin/activate
```

Prepare the test database:
```bash
$ dropdb sealmess_test
$ createdb sealmess_test
$ psql sealmess_test < src/database/sealmess_test_db.psql
```

To run the unittests, execute:
```bash
$ source setup_test.sh
$ python3 -m unittest run_tests.py -v
```


## General Information
### Data Modeling

#### Classes
It requires four classes, with one-to-many and many-to-many relationships between them:
* customers
* providers
* meal-items
* orders

##### Tables

* **PK**: Primary Key
* **FK**: Foreign Key

| customers     | providers    | menu_items           | orders                  | order_items *(Association table)* | 
| ------------- |------------- | ---------------------|-------------------------|-----------------------------------|
| **id** (PK)   | **id** (PK)  | **id** (PK)          | **id** (PK)             | **order_id** (FK)                 | 
| first_name    | name         | **provider_id** (FK) | **customer_id** (FK)    | **menu_item_id** (FK)             |
| last_name     | address      | name                 | status                  |                                   |
| address       | phone        | description          | created_at              |                                   |
| phone         | description  | price                |                         |                                   |
|               | image_link   | image_link           |                         |                                   |  

# API Architecture
## Getting Started
The app can be run locally, hosted by default at http://localhost:5000, or it can be tested live at https://sealmess.herokuapp.com/.

## Third-Party Authentication
There are three roles that have different RBAC:
* customer
* provider
* owner

To create JWT access tokens in order to test the endpoints manually, one can run:
```bash
$ python3 src/tests/config.py
```
which will print out the access tokens.

Assume you copy one of the access tokens into an environment variable like this for example:
```bash
CUSTOMER_ACCESS_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik4wVXdOamxFTjBZMFJFSTFRa1ExT0RZeU56WXdOa1F3UkRZNU1VRkZNalJHTkVZME16RkZSQSJ9.eyJpc3MiOiJodHRwczovL2Rldi05cnFoMnRpYi5hdXRoMC5jb20vIiwic3ViIjoiT3daajVZUXFFN2tSUmhJNmY2S3RqbVdpMGdrMURwVGxAY2xpZW50cyIsImF1ZCI6InNlYWxtZXNzIiwiaWF0IjoxNTg3Njg4NTMxLCJleHAiOjE1ODc3NzQ5MzEsImF6cCI6Ik93Wmo1WVFxRTdrUlJoSTZmNkt0am1XaTBnazFEcFRsIiwic2NvcGUiOiJwb3N0OmN1c3RvbWVyIGdldDpjdXN0b21lciBwYXRjaDpjdXN0b21lciBkZWxldGU6Y3VzdG9tZXIgcG9zdDpvcmRlciBnZXQ6b3JkZXIgZGVsZXRlOm9yZGVyIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOlsicG9zdDpjdXN0b21lciIsImdldDpjdXN0b21lciIsInBhdGNoOmN1c3RvbWVyIiwiZGVsZXRlOmN1c3RvbWVyIiwicG9zdDpvcmRlciIsImdldDpvcmRlciIsImRlbGV0ZTpvcmRlciJdfQ.TRJyZh5MzSAu77Plf5bydKtX84EdaMUsbgtogKv1Zz1SIZIeeEP-kgfaA8Ns6LCvFTMoknRJ_0q1kpxsg7IU0ZJwiZHQ8HTVio4tsLSIYTPTv_i-Tsws201zsWwho4sLm7J1AwdyZU4EBFhQzpuUpPxt5nXo46DoyM2gADYNhj2oWx_HsQ43hCLuBA4UgpLUQ0oADrgo3tGGr6uf-f3FWXKJEMADXQrVCdZLNUF6uckG0FFPFrk9sZBfGH9kjzn29_3GBR_TYcqaPlmFiUZw-5dbIKhZp9mDBNRRI74OxUvsgNMInG2OUfPtntvSnFGsC_jPMVle2VP6VXFc9lwIbw'
```

One can then go ahead and test one of the endpoints using `curl` like this:
```bash
curl --request GET \
  --url https://sealmess.herokuapp.com/customers/1 \
  --header "authorization: Bearer ${CUSTOMER_ACCESS_TOKEN}"
```

## Endpoints
* Overview of relative endpoints:
  * GET
    * /
    * /createdata
    * /customers/<int:customer_id>
    * /customers/<int:customer_id>/orders
    * /customers/<int:customer_id>/orders/<int:order_id>
    * /providers
    * /providers/<int:provider_id>
    * /providers/<int:provider_id>/menu
    * /providers/<int:provider_id>/menu/<int:menu_item_id>
  * POST
    * /customers
    * /customers/<int:customer_id>/orders
    * /orders/<int:order_id>/menu_items
    * /providers
    * /providers/<int:provider_id>/menu
  * PATCH
    * /customers/<int:customer_id>
    * /providers/<int:provider_id>
    * /providers/<int:provider_id>/menu/<int:menu_item_id>
  * DELETE
    * /customers/<int:customer_id>
    * /customers/<int:customer_id>/orders/<int:order_id>
    * /providers/<int:provider_id>
    * /providers/<int:provider_id>/menu/<int:menu_item_id>


# Customer
curl --request GET \
  --url https://sealmess.herokuapp.com/customers/1 \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik4wVXdOamxFTjBZMFJFSTFRa1ExT0RZeU56WXdOa1F3UkRZNU1VRkZNalJHTkVZME16RkZSQSJ9.eyJpc3MiOiJodHRwczovL2Rldi05cnFoMnRpYi5hdXRoMC5jb20vIiwic3ViIjoiT3daajVZUXFFN2tSUmhJNmY2S3RqbVdpMGdrMURwVGxAY2xpZW50cyIsImF1ZCI6InNlYWxtZXNzIiwiaWF0IjoxNTg3NjY1NzQyLCJleHAiOjE1ODc3NTIxNDIsImF6cCI6Ik93Wmo1WVFxRTdrUlJoSTZmNkt0am1XaTBnazFEcFRsIiwic2NvcGUiOiJwb3N0OmN1c3RvbWVyIGdldDpjdXN0b21lciBwYXRjaDpjdXN0b21lciBkZWxldGU6Y3VzdG9tZXIgcG9zdDpvcmRlciBnZXQ6b3JkZXIgZGVsZXRlOm9yZGVyIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOlsicG9zdDpjdXN0b21lciIsImdldDpjdXN0b21lciIsInBhdGNoOmN1c3RvbWVyIiwiZGVsZXRlOmN1c3RvbWVyIiwicG9zdDpvcmRlciIsImdldDpvcmRlciIsImRlbGV0ZTpvcmRlciJdfQ.grv-iwXrAmv6h-XBIN-3ZKyxUd_0nM-p2tnhJ2l1ZM2D1qoA2GQk2oHjzrs7qAHEnBPUq0GC6d89uuzRoMHigbioXumSxvE1ZqeK1-R78n8cvnUJem_Q0tlqoBOKCmljfDc6-1RUPoxen7RpTKr-VkO2iGQ1TEc-7JAQviliyPOffYMbQf8M9RseK5HdwbGdEV1LSwsro8f-vZ9IHte0ts5388MdhjbzTdCTMgEQiieeX8qEaJT5kiTykQL0ntaF4JEIoywTWazU0iT1e2lSnrWsbqgVIwRB4pvoheHhNpx4jFYbFi_UmKO63pvXB0mQAf02aVKRCbcpz_bbyL7R2w'

# Owner
  curl --request GET \
  --url https://sealmess.herokuapp.com/customers/1 \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik4wVXdOamxFTjBZMFJFSTFRa1ExT0RZeU56WXdOa1F3UkRZNU1VRkZNalJHTkVZME16RkZSQSJ9.eyJpc3MiOiJodHRwczovL2Rldi05cnFoMnRpYi5hdXRoMC5jb20vIiwic3ViIjoidXd6MHhVbWU0eXVaMHEyRmM5bW5FQkFoTkY1bjNIRHVAY2xpZW50cyIsImF1ZCI6InNlYWxtZXNzIiwiaWF0IjoxNTg3NjY2MTg0LCJleHAiOjE1ODc3NTI1ODQsImF6cCI6InV3ejB4VW1lNHl1WjBxMkZjOW1uRUJBaE5GNW4zSER1Iiwic2NvcGUiOiJkZWxldGU6cHJvdmlkZXIiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cHJvdmlkZXIiXX0.Up0gkdISLGANS-V5UrjclJ9JB9N8lqxsFlnI4wZsBYA-7StyAEkVYqf8HRaxypYTapKDCp9XpFGH-74cGcYv2AgrQCcoLNFv8FKGzLzJVxfpU-lkbBkFqWKGqLj63xtgJGHafEQVS6zpuvMxlXiS3Er75spEP1Cs-qP3TYxgljxfZBrui3YzOM_TqxzMVX6zd3EnG7LeUqipvZgS0udAPLYmUYKUFP1ng77SfotfBM4qfaX42bGHDFjWCevpxdrRKPEh1TeTESmY3wAJ3Mj81KTn8r92aA06K5uMJG-mbQPrWWUIJA6Xvjrl-ZDxw4bEceK8VffDBV-cSMJfIQCIPw'
  
