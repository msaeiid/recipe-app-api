# Advanced Backend REST API with Django, Django REST Framework, and Docker

Welcome to the **Advanced Backend REST API** project built using **Django**, **Django REST Framework**, **Docker**, and **Test Driven Development** (TDD). This repository is based on Build a Backend REST API with Python & Django - Advanced that covers the development of a REST API with advanced features such as user authentication, creating objects, uploading and viewing images, and much more.

## Project Overview

In this project, we will be building an advanced **Recipe API**. This API will allow users to create and manage recipes, categorize them with tags, filter through them, and upload related images. The project follows **Test Driven Development** (TDD) and implements **best practices** such as **PEP-8**, **unit tests**, and **GitHub Actions** for continuous integration.

### Key Features
- **User Authentication**: Create and manage user profiles, login/logout, and change passwords.
- **Recipe Management**: Create, update, delete, and retrieve recipes with detailed attributes such as title, price, ingredients, and cooking time.
- **Tagging System**: Add tags to recipes (e.g., "vegan", "comfort food").
- **Image Upload**: Upload images related to recipes and view them.
- **Advanced Filtering and Sorting**: Filter recipes by tags, ingredients, and more.
- **Dockerized Development Environment**: Utilize Docker and Docker-Compose to easily set up the local development environment.
- **Unit Tests**: Test the application using Django's testing framework with TDD approach.
- **Postgres Database**: Integrate a PostgreSQL database for storing data.
- **Continuous Integration**: Configure GitHub Actions for linting and running unit tests automatically.

## Tech Stack
- **Django 3.2**
- **Django REST Framework 3.12**
- **Docker**
- **PostgreSQL**
- **GitHub Actions**
- **Test Driven Development (TDD)**

## Installation

### Prerequisites
- Docker and Docker-Compose installed
- Python 3.8+
- Git

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/advanced-backend-api.git
   cd advanced-backend-api
   ```

2. Build and start the Docker containers:
   ```bash
   docker-compose up --build
   ```

3. Apply the migrations:
   ```bash
   docker-compose run app python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   docker-compose run app python manage.py createsuperuser
   ```

5. Run the project:
   ```bash
   docker-compose up
   ```

The API will now be accessible at `http://localhost:8000/`.

## Running Tests

The project follows **Test Driven Development** principles, and tests are an integral part of the development process.

To run tests, use the following command:
```bash
docker-compose run app python manage.py test
```

You can also check the code for PEP-8 linting using:
```bash
docker-compose run app flake8
```

## Docker Setup

This project uses Docker to create an isolated development environment. **Docker-Compose** is used to configure the application services, including a **Postgres** database. You can modify the `docker-compose.yml` and `.env` files to fit your own setup.

### Available Docker Commands
- Start the application: `docker-compose up`
- Stop the application: `docker-compose down`
- Rebuild the containers: `docker-compose up --build`
- Run management commands (e.g., migrations): `docker-compose run app python manage.py <command>`

## Course Description

This repository is part of an advanced course on how to build a **Backend REST API** using **Python**, **Django**, **Django REST Framework**, **Docker**, **GitHub Actions**, **Postgres**, and **Test Driven Development**. The course is designed to give you hands-on experience in building a fully functioning REST API, with best practice principles applied throughout the project.

Some of the core concepts covered include:

- Setting up a local development environment with Docker
- Writing Python projects using TDD
- Building an advanced REST API with features like image uploading and viewing
- Applying industry best practices such as PEP-8 and unit testing

### Who Is This Course For?
- **Intermediate Python developers** looking to enhance their backend development skills.
- **Developers from other programming languages** who want to learn Python and Django for backend development.

### What You Will Learn
- **Creating an advanced REST API** from scratch
- **TDD and unit testing** to ensure code quality
- **Docker setup** for a seamless development environment
- **GitHub Actions** for automating tests and linting
- **Best practices** for writing clean and efficient code

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.


---

Thank you for checking out this project! If you have any questions or issues, feel free to open an issue or contact me via GitHub.
