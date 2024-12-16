[PYTHON_BADGE]: https://img.shields.io/badge/python-fff?style=for-the-badge&logo=python
[DJANGO_BADGE]: https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django

<h1 align="center">CodeLeap API</h1>

<div align="center">
  <strong>Code challenge for CodeLeap</strong>
</div>

<div align="center">
  <p>An amazing repository with a spectacular project! 🎉</p>
</div>

## 📖 Table of Contents

- [📖 Table of Contents](#-table-of-contents)
- [🔭 Overview](#-overview)
- [⚙️ Project Setup](#️-project-setup)
- [🧪 Running Tests](#-running-tests)
- [🌍 Deploy](#-deploy)

## 🔭 Overview

![python][PYTHON_BADGE]
![django][DJANGO_BADGE]

This repository is a simple social network API designed to handle posts. It is built using Django and Django Rest Framework (DRF). The API allows users to create, retrieve, update, and delete posts. The project demonstrates the use of Django and DRF for building robust and scalable backend solutions.

Additionally, the project includes **Swagger** documentation for the API, generated with the help of **drf-spectacular**, providing an interactive UI for testing and exploring the API endpoints.

## ⚙️ Project Setup

1. Clone the repository

```
git clone https://github.com/titofrota/codeleap-api.git
```

2. Navigate to the project directory

```
cd codeleap-api
```

3. Install the required dependencies

```
pip install -r requirements.txt
```

4. Make migrations
```
python manage.py makemigrations
```

5. Run migrations
```
python manage.py migrate
```

6. Run the server
```
python manage.py runserver
```

## 🧪 Running Tests

To run the tests for this project, use the following command:

```
pytest
```

Make sure to have all the dependencies installed and the database migrated before running the tests.

## 🌍 Deploy

The challenge is hosted at: [codeleap-drce.onrender.com/api/v1/](https://codeleap-drce.onrender.com/api/v1/)

You can visit this URL to explore the API documentation using Swagger UI:

- **Swagger UI**: [api/schema/swagger-ui/](https://codeleap-drce.onrender.com/api/schema/swagger-ui/)
- **Redoc**: [api/schema/redoc/](https://codeleap-drce.onrender.com/api/schema/redoc/)

The API provides all the necessary endpoints to interact with the social network and test its functionalities.
