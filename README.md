# Travel Guru App
The Travel Guru App is a FastAPI application that provides an API for managing users and destinations. It allows users to retrieve all users, retrieve all destinations, delete a user, and delete a destination. The app utilizes SQLAlchemy for database operations and provides JSON responses.

### Prerequisites
Before running the Travel Guru App, make sure you have the following installed:

Python (version 3.6 or later)
pip (Python package installer)

### Installation
Clone the repository or download the source code files.

Open a terminal and navigate to the project's root directory.

Install the required dependencies by running the following command:

pipenv install; pipenv shell


## Database Configuration
The Travel Guru App uses an SQLite database. The database is defined in the models.py file and can be found at project.db. If you want to use a different database, make sure to update the SQLAlchemy configuration in the code.

## Usage
To run the Travel Guru App, follow these steps:

Make sure you are in the project's root directory in the terminal.

Start the FastAPI server by running the following command:

uvicorn main:app --reload
Open a web browser and access the API at http://localhost:8000.

## API Endpoints
The Travel Guru App exposes the following API endpoints:

GET /: Returns a welcome message for the user.

GET /users: Retrieves all users from the database.

GET /destinations: Retrieves all destinations from the database.

DELETE /users/{id}: Deletes a user with the specified ID.

DELETE /destinations/{id}: Deletes a destination with the specified ID.

## Data Models
The Travel Guru App defines the following data models:

## Users
The Users model represents a user in the application. It has the following attributes:

id: The unique identifier for the user.
name: The name of the user.
password: The password of the user.
Destinations
The Destinations model represents a travel destination in the application. It has the following attributes:

id: The unique identifier for the destination.
name: The name of the destination.
image: The URL of the destination image.
description: The description of the destination.
location: The location of the destination.
visit_url: The URL for visiting the destination.
interested: A boolean indicating whether the destination is of interest.
user_id: The ID of the user associated with the destination.

## Database Interaction
The Travel Guru App uses SQLAlchemy for interacting with the database. The database connection and session management are handled in the models.py file. The session object is used to query and manipulate data.

### Dependencies
The Travel Guru App has the following dependencies:

FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.
SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.

## MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.