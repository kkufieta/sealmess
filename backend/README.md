# Backend

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
python3 -m unittest
```
