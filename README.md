# sealmess - Meal delivery service
This is the Capstone Project for the [Fullstack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044) at Udacity. 

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
  
## Backend
Read the [Backend README](https://github.com/kkufieta/sealmess/blob/master/backend/README.md)

## Frontend
The frontend has not been implemented yet.

## Tech Stack

The tech stack includes:

* **SQLAlchemy ORM**: ORM library
* **PostgreSQL**: database
* **Python3** and **Flask**: server language and server framework
* **Flask-Migrate**: for creating and running schema migrations
* **unittest**: Python unittesting framework to test the endpoints
