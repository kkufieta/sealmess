# Sealmess Backend

## Table of Contents
* [Live Deployment on Heroku](https://github.com/kkufieta/sealmess/blob/master/backend/README.md#live-deployment-on-heroku)
* [Development Setup](https://github.com/kkufieta/sealmess/blob/master/backend/README.md#development-setup)
  * [Python 3.7](https://github.com/kkufieta/sealmess/blob/master/backend/README.md#python-37)
  * [Virtual Environment](https://github.com/kkufieta/sealmess/blob/master/backend/README.md#virtual-enviornment)
  * [Install Dependencies](https://github.com/kkufieta/sealmess/blob/master/backend/README.md#install-dependencies)
* [Database Setup](https://github.com/kkufieta/sealmess/blob/master/backend/README.md#database-setup)
  * [Migrations](https://github.com/kkufieta/sealmess/blob/master/backend/README.md#migrations)
  * [Reset Database](https://github.com/kkufieta/sealmess/blob/master/backend/README.md#reset-database)
* [Testing](https://github.com/kkufieta/sealmess/blob/master/backend/README.md#testing)
* [API Architecture](https://github.com/kkufieta/sealmess/blob/master/backend/README.md#api-architecture)
  * [General Information](https://github.com/kkufieta/sealmess/blob/master/backend/README.md#general-information)
  * [Getting Started](https://github.com/kkufieta/sealmess/blob/master/backend/README.md#getting-started)
  * [Third-Party Authentication](https://github.com/kkufieta/sealmess/blob/master/backend/README.md#third-party-authentication)
  * [Endpoints](https://github.com/kkufieta/sealmess/blob/master/backend/README.md#endpoints)
    * [Overview](https://github.com/kkufieta/sealmess/blob/master/backend/README.md#overview)
    * [Detailed Information and Examples](https://github.com/kkufieta/sealmess/blob/master/backend/README.md#detailed-information-and-examples)


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




# API Architecture

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

## Getting Started
The app can be run locally, hosted by default at http://localhost:5000, or it can be tested live at https://sealmess.herokuapp.com/.

## Third-Party Authentication
There are three roles that have different RBAC:
* customer
* provider
* owner

To create JWT access tokens in order to test the endpoints manually, one can run:
```bash
$ source setup_test.sh
$ python3 src/tests/config.py
```
which will print out the access tokens ready to be copy-pasted into the terminal to load them as environment variables, which will look like this (with real access tokens):
```bash
CUSTOMER_ACCESS_TOKEN="...."
PROVIDER_ACCESS_TOKEN="..."
OWNER_ACCESS_TOKEN="..."
```
Copy & paste that output into your terminal to load the access tokens into environment variables.

One can then go ahead and test one of the endpoints using `curl` like this:
```bash
curl --request GET \
  --url https://sealmess.herokuapp.com/customers/1 \
  --header "authorization: Bearer ${CUSTOMER_ACCESS_TOKEN}"
```

## Endpoints
### Overview
  * GET
    * /
    * /createdata
    * /customers/{int:customer_id}
    * /customers/{int:customer_id}/orders
    * /customers/{int:customer_id}/orders/{int:order_id}
    * /providers
    * /providers/{int:provider_id}
    * /providers/{int:provider_id}/menu
    * /providers/{int:provider_id}/menu/{int:menu_item_id}
  * POST
    * /customers
    * /customers/{int:customer_id}/orders
    * /orders/{int:order_id}/menu_items
    * /providers
    * /providers/{int:provider_id}/menu
  * PATCH
    * /customers/{int:customer_id}
    * /providers/{int:provider_id}
    * /providers/{int:provider_id}/menu/{int:menu_item_id}
  * DELETE
    * /customers/{int:customer_id}
    * /customers/{int:customer_id}/orders/{int:order_id}
    * /providers/{int:provider_id}
    * /providers/{int:provider_id}/menu/{int:menu_item_id}

### Detailed Information and Examples
#### GET /
* General:
  * Welcome Homepage, and a sanity check to see if the app runs.
* Sample: `curl https://sealmess.herokuapp.com`

#### GET /createdata
* General:
  * For the convenience of a developer, to populate & add data into the DB.
* Sample: `curl https://sealmess.herokuapp.com/createdata`

#### GET /customers/{int:customer_id}
* General:
  * Get information about a specific customer
  * RBAC: Customer
* Sample:
```bash
curl --request GET \
  --url https://sealmess.herokuapp.com/customers/1 \
  --header "authorization: Bearer ${CUSTOMER_ACCESS_TOKEN}"
```

#### GET /customers/{int:customer_id}/orders
* General:
  * Get the orders from a specific customer
  * RBAC: Customer
* Sample:
```bash
curl --request GET \
  --url https://sealmess.herokuapp.com/customers/1/orders \
  --header "authorization: Bearer ${CUSTOMER_ACCESS_TOKEN}"
```

#### GET /customers/{int:customer_id}/orders/{int:order_id}
* General:
  * Get a specific order from a specific customer
  * RBAC: Customer
* Sample:
```bash
curl --request GET \
  --url https://sealmess.herokuapp.com/customers/1/orders/1 \
  --header "authorization: Bearer ${CUSTOMER_ACCESS_TOKEN}"
```

#### GET /providers
* General:
  * Get a list of providers
* Sample: `curl https://sealmess.herokuapp.com/providers`

#### GET /providers/{int:provider_id}
* General:
  * Get a specific provider
* Sample: `curl https://sealmess.herokuapp.com/providers/1`

#### GET /providers/{int:provider_id}/menu
* General:
  * Get the menu of a specific provider
* Sample: `curl https://sealmess.herokuapp.com/providers/1/menu`

#### GET /providers/{int:provider_id}/menu/{int:menu_item}
* General:
  * Get a specific menu item of the menu of a specific provider
* Sample: `curl https://sealmess.herokuapp.com/providers/1/menu/1`

#### POST /customers
* General:
  * Add a customer
  * RBAC: Customer
* Sample:
```bash
curl --request POST \
  --url https://sealmess.herokuapp.com/customers \
  --header "authorization: Bearer ${CUSTOMER_ACCESS_TOKEN}" \
  --header "Content-Type: application/json" \
  --data '{"first_name": "kat", "last_name": "kk", "address": "home", "phone": "xxx"}'
```

#### POST /customers/{int:customer_id}/orders
* General:
  * Add a new order to a specific customer
  * RBAC: Customer
* Sample:
```bash
curl --request POST \
  --url https://sealmess.herokuapp.com/customers/1/orders \
  --header "authorization: Bearer ${CUSTOMER_ACCESS_TOKEN}" \
  --header "Content-Type: application/json" \
  --data '{"customer_id": 1, "status": "eaten", "menu_item_ids": []}'
```

#### POST /orders/{int:order_id}/menu_items
* General:
  * Add a new menu item to an existing order
  * RBAC: Customer
* Sample:
```bash
curl --request POST \
  --url https://sealmess.herokuapp.com/orders/21/menu_items \
  --header "authorization: Bearer ${CUSTOMER_ACCESS_TOKEN}" \
  --header "Content-Type: application/json" \
  --data '{"menu_item_ids": [3]}'
```

#### POST /providers
* General:
  * Add a new provider
  * RBAC: Provider
* Sample:
```bash
curl --request POST \
  --url https://sealmess.herokuapp.com/providers \
  --header "authorization: Bearer ${PROVIDER_ACCESS_TOKEN}" \
  --header "Content-Type: application/json" \
  --data '{"name": "Sushi", "address": "Around the Corner", "phone": "sss", "description": "Delicious!"}'
```

#### POST /providers/{int:provider_id}/menu
* General:
  * Add a new menu item to a specific provider
  * RBAC: Provider
* Sample:
```bash
curl --request POST \
  --url https://sealmess.herokuapp.com/providers/1/menu \
  --header "authorization: Bearer ${PROVIDER_ACCESS_TOKEN}" \
  --header "Content-Type: application/json" \
  --data '{"provider_id": 1, "name": "New Food Item!", "description": "so good..", "price": 12.12}'
```

#### PATCH /customers/{int:customer_id}
* General:
  * Edit a specific customer
  * RBAC: Customer
* Sample:
```bash
curl --request PATCH \
  --url https://sealmess.herokuapp.com/customers/1 \
  --header "authorization: Bearer ${CUSTOMER_ACCESS_TOKEN}" \
  --header "Content-Type: application/json" \
  --data '{"first_name": "KITTYKAT"}'
```

#### PATCH /providers/{int:provider_id}
* General:
  * Edit a specific provider
  * RBAC: Provider
* Sample:
```bash
curl --request PATCH \
  --url https://sealmess.herokuapp.com/providers/1 \
  --header "authorization: Bearer ${PROVIDER_ACCESS_TOKEN}" \
  --header "Content-Type: application/json" \
  --data '{"name": "Bayrische Kueche Ist Die Beste!"}'
```

#### PATCH /providers/{int:provider_id}/menu/{int:menu_item_id}
* General:
  * Edit a specific menu item on the menu of a specific provider
  * RBAC: Provider
* Sample:
```bash
curl --request PATCH \
  --url https://sealmess.herokuapp.com/providers/2/menu/3 \
  --header "authorization: Bearer ${PROVIDER_ACCESS_TOKEN}" \
  --header "Content-Type: application/json" \
  --data '{"description": "Short ribs are delicious!"}'
```

#### DELETE /customers/{int:customer_id}
* General:
  * Delete a specific customer
  * RBAC: Customer
* Sample:
```bash
curl --request DELETE \
  --url https://sealmess.herokuapp.com/customers/3 \
  --header "authorization: Bearer ${CUSTOMER_ACCESS_TOKEN}"
```

#### DELETE /customers/{int:customer_id}/orders/{int:order_id}
* General:
  * Delete a specific order from a specific customer
  * RBAC: Customer
* Sample:
```bash
curl --request DELETE \
  --url https://sealmess.herokuapp.com/customers/4/orders/23 \
  --header "authorization: Bearer ${CUSTOMER_ACCESS_TOKEN}"
```


#### DELETE /providers/{int:provider_id}
* General:
  * Delete a specific provider
  * RBAC: Provider, Owner
* Sample:
```bash
curl --request DELETE \
  --url https://sealmess.herokuapp.com/providers/14 \
  --header "authorization: Bearer ${OWNER_ACCESS_TOKEN}"
```

#### DELETE /providers/{int:provider_id}/menu/{int:menu_item_id}
* General:
  * Delete a specific menu_item from a specific providers menu
  * RBAC: Provider
* Sample:
```bash
curl --request DELETE \
  --url https://sealmess.herokuapp.com/providers/10/menu/34 \
  --header "authorization: Bearer ${PROVIDER_ACCESS_TOKEN}"
```
