# Capstone Project: SealMess
This is the Capstone Project for the Fullstack Web Developer Nanodegree at Udacity. 

For this project, I chose to implement a simplified meal delivery service inspired by Seamless.

## Requirements
General Specifications
* Models will include at least…
  * Two classes with primary keys at at least two attributes each
  * [Optional but encouraged] One-to-many or many-to-many relationships between classes
* Endpoints will include at least…
  * Two GET requests
  * One POST request
  * One PATCH request
  * One DELETE request
* Roles will include at least…
  * Two roles with different permissions
  * Permissions specified for all endpoints
* Tests will include at least….
  * One test for success behavior of each endpoint
  * One test for error behavior of each endpoint
  * At least two tests of RBAC for each role


## Description
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

### Data
* PostgreSQL database for storing, querying, and creating information about customers and their favorite menu items, as well as providers with their menus.
* Build data models to power the API endpoints for SealMess.

### Tech Stack

The tech stack includes:

* **SQLAlchemy ORM** to be our ORM library of choice
* **PostgreSQL** as our database of choice
* **Python3** and **Flask** as our server language and server framework
* **Flask-Migrate** for creating and running schema migrations
[//]: # * **HTML**, **CSS**, and **Javascript** with [Bootstrap 3](https://getbootstrap.com/docs/3.4/customize/) for our website's frontend

### Main Files: Project Structure

  ```sh
  ├── README.md
  ├── app.py *** the main driver of the app. Includes your SQLAlchemy models.
                    "python app.py" to run after installing dependences
  ├── config.py *** Database URLs, CSRF generation, etc
  ├── error.log
  ├── forms.py *** Your forms
  ├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
  ```

Overall:
* Models are located in the `MODELS` section of `app.py`.
* Controllers are also located in `app.py`.
* Web forms for creating data are located in `form.py`


Highlight folders:
* `app.py` -- (Missing functionality.) Defines routes that match the user’s URL, and controllers which handle data and renders views to the user. This is the main file you will be working on to connect to and manipulate the database and render views with data to the user, based on the URL.
* Models in `app.py` -- (Missing functionality.) Defines the data models that set up the database tables.
* `config.py` -- (Missing functionality.) Stores configuration variables and instructions, separate from the main application code. This is where you will need to connect to the database.


My Plan broken down into action items
-----

1. Build the app:
  1. Plan out the app and its functionality. Describe your app and implementation steps & requirements in the README.
  2. Model the database tables and their relationships (one-to-one, one-to-many, many-to-many)
  3. Create two seed databases: One for testing, and one for development.
  3. Write error handlers.
  4. Write tests for all endpoints. Create a Postman collection.
  5. Write all endpoints while testing frequently.
  6. Create an Auth0 app & API for this application, add roles: customer, provider, owner.
  7. Write error handlers for authentication & identification.
  8. Write tests that include the different roles & permissions.
  9. Implement authentication & identification helper functions, make sure to assign requirements to all endpoints.
  10. Rinse and repeat until all functionality is implemented and passes all tests. Document as best as you can while working on everything.
  11. Once all endpoints are implemented and pass the tests successfully, deploy the app on Heroku.
  12. Create a continuous delivery pipeline. Test it.
  13. Test everything once more, improve documentation, submit project. Fix issues from code review until you pass.
  14. Celebrate!
2. Build and run local development following the Development Setup steps below.
3. Fill out every `TODO` section throughout the codebase. We suggest going in order of the following:

  1. Connect to a database in `config.py`. A project submission that uses a local database connection is fine.
  2. Using SQLAlchemy, set up normalized models for the objects we support in our web app in the Models section of `app.py`. Use all of the learned best practices in database schema design. Implement missing model properties and relationships using database migrations via Flask-Migrate.
  3. Implement form submissions for creating new Venues, Artists, and Shows. There should be proper constraints, powering the `/create` endpoints that serve the create form templates, to avoid duplicate or nonsensical form submissions. Submitting a form should create proper new records in the database.
  4. Implement the controllers for listing venues, artists, and shows. Note the structure of the mock data used. We want to keep the structure of the mock data.
  5. Implement search for providers and menu-items, powering the `/search` endpoints that serve the application's search functionalities.
  6. Serve customer and provider detail pages, powering the `<customer|provider>/<id>` endpoints that power the detail pages.


Acceptance Criteria
-----

1. The web app should be successfully connected to a PostgreSQL database. A local connection to a database on your local computer is fine.
2. There should be no use of mock data throughout the app. The data structure of the mock data per controller should be kept unmodified when satisfied by real data.
3. The application should behave just as before with mock data, but now uses real data from a real backend server, with real search functionality. 
4. As a fellow developer on this application, I should be able to run `flask db migrate`, and have my local database (once set up and created) be populated with the right tables to run this application and have it interact with my local postgres server, serving the application's needs completely with real data I can seed my local database with.
  * The models should be completed (see TODOs in the `Models` section of `app.py`) and model the objects used throughout Fyyur.
  * The right _type_ of relationship and parent-child dynamics between models should be accurately identified and fit the needs of this particular application.
  * The relationship between the models should be accurately configured, and referential integrity amongst the models should be preserved.
  * `flask db migrate` should work, and populate my local postgres database with properly configured tables for this application's objects, including proper columns, column data types, constraints, defaults, and relationships that completely satisfy the needs of this application. The proper type of relationship between customers, providers, and menu items should be configured.

##### Stand Out

Looking to go above and beyond? This is the right section for you! Here are some challenges to make your submission stand out:

*  Implement a frontend to visualize all the hard work!


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
