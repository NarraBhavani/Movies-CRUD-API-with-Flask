# Movies-CRUD-API-with-Flask
Film Blog using Flask and PostgreSQL

This is a simple web application for a film blog built with Flask, a Python web framework, and PostgreSQL, a relational database.
The blog allows users to view and create blog posts about their favorite films.

Prerequisites

Before you begin, ensure you have met the following requirements:

Python 3.7 or higher installed.

PostgreSQL database server installed and running.

Basic knowledge of Flask, SQLAlchemy, and HTML/CSS.

Installation

Clone this repository:

git clone https://github.com/yourusername/film-blog-flask.git

Change into the project directory:

cd film-blog-flask

Create a virtual environment and activate it:

python -m venv venv

source venv/bin/activate  # On Windows, use "venv\Scripts\activate"

Install the required Python packages:

pip install -r requirements.txt

Set up the PostgreSQL database:

Create a PostgreSQL database for your project.

Update the database configuration in config.py.

Apply the database migrations:
flask db upgrade

Run the application:
flask run

Usage

Open your web browser and navigate to http://localhost:5000.

You can view existing blog posts, create a new post, and edit/delete your posts.


Project Structure

The project directory structure is as follows:

app/: Contains the main application code.

models/: Defines SQLAlchemy models for the database.

routes/: Defines URL routes and views.

templates/: HTML templates for rendering pages.

static/: Static files like CSS and JavaScript.

config.py: Configuration settings for the application.

run.py: The entry point to start the Flask application.

requirements.txt: Lists the required Python packages.

migrations/: Stores database migration files.







