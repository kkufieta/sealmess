# SealMess - Meal delivery service
This is the Capstone Project for the Fullstack Web Developer Nanodegree at Udacity. 

For this project, I chose to implement a simplified meal delivery service inspired by Seamless.

## Motivation
I wanted to create a simplified version of Seamless, which would include the following:
### Roles, RBAC
* Customers
  * Can sign up, view, edit & delete their own profiles
  * Can view providers and their menus
  * Create orders with the menu items from the providers
  * Add more menu items to an order
  * Delete orders
* Providers
  * Can sign up, view, edit & delete their own profiles
  * Can add, edit, and delete menu items to/from their menus
* Owner
  * The owner of the website can delete providers (e.g. in case of violations)
  
### Classes
It requires four classes, with one-to-many and many-to-many relationships between them:
* customers
* providers
* meal-items
* orders

### Tables
**PK**: Primary Key
**FK**: Foreign Key

| customers     | providers    | menu_items           | orders                  | order_items *(Association table)* | 
| ------------- |------------- | ---------------------|-------------------------|-----------------------------------|
| **id (PK)**   | **id (PK)**  | **id (PK)**          | **id (PK)**             | **order_id (FK)**                 | 
| first_name    | name         | **provider_id (FK)** | **customer_id (FK)**    | **menu_item_id (FK)**             |
| last_name     | address      | name                 | status                  |                                   |
| address       | phone        | description          | created_at              |                                   |
| phone         | description  | price                |                         |                                   |
|               | image_link   | image_link           |                         |                                   |  

## Tech Stack

The tech stack includes:

* **SQLAlchemy ORM**: ORM library
* **PostgreSQL**: database
* **Python3** and **Flask**: server language and server framework
* **Flask-Migrate**: for creating and running schema migrations

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
