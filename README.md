[PYTHON_BADGE]: https://img.shields.io/badge/python-fff?style=for-the-badge&logo=python
[DJANGO_BADGE]: https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django

<h1 align="center">CodeLeap API</h1>

<div align="center">
  <strong>Code challenge for CodeLeap</strong>
</div>

## 📖 Table of Contents

- [📖 Table of Contents](#-table-of-contents)
- [🔭 Overview](#-overview)
- [⚙️ Project Setup](#️-project-setup)
- [🧪 Running Tests](#-running-tests)
- [🌍 Deploy](#-deploy)
- [🛠️ Implementation Process](#️-implementation-process)
  - [💡 Lessons Learned](#-lessons-learned)

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

![image](https://github.com/user-attachments/assets/0a5fb77f-db50-4458-8131-5fef4003949e)

---

## 🛠️ Implementation Process

This was my first time implementing a project with Django, and it was quite a learning journey. Since I had little prior experience with Django, I started by diving into the documentation and understanding the key concepts, such as models, views, serializers, and how the Django Rest Framework (DRF) works. I wanted to get a solid grasp of the framework before moving into the actual implementation.

Once I felt comfortable with the basics, I began thinking about the project’s architecture. My initial plan was to introduce a service layer to keep business logic decoupled from the rest of the application. However, when I started working on the views, I came across viewsets, and the simplicity and power they offered in handling both create, update, and retrieve actions changed my mind. Instead of using function-based views, class-based views, or even APIView, I decided to embrace viewsets. Their built-in functionality for handling common actions like list, create, update, and delete was perfect for this project’s simplicity, and it allowed me to reduce boilerplate code significantly.

By opting for viewsets, I ended up eliminating the need for a service layer, as viewsets themselves encapsulated the necessary logic in a clean and manageable way. I then moved on to implement the serializers to transform data between JSON and Python objects.

Next, I set up the routes for the API. With Django and DRF, setting up URL routing was straightforward and helped me organize the API endpoints clearly.

Once the core functionality was in place, I focused on testing. While I didn’t follow TDD (Test-Driven Development) for this project, I felt more comfortable jumping straight into the implementation. My priority was to get familiar with Django’s structure and workflows first, so I opted to implement the features first and then test the code after. I plan to improve my testing approach as I continue to gain more experience with Django.

To document the API and improve usability, I added Swagger using DRF-Spectacular. This made it easy to visualize and interact with the API directly in the browser, which was incredibly helpful for both testing and providing clear documentation.

Finally, I configured the project for deployment, ensuring everything would run smoothly in a production environment. After completing the project, I reviewed my work and the steps I took throughout the process.

### 💡 Lessons Learned

- **Simplicity is powerful**: Viewsets in DRF made it easy to manage complex API actions without needing to overcomplicate the design. I learned to embrace Django’s built-in tools and use them to my advantage.
  
- **Start small, grow big**: Even though I initially planned for a service layer, I realized that simplifying the architecture allowed for quicker iteration and learning. I can always refactor and add complexity later if needed.

- **Testing will improve over time**: Although I didn’t follow TDD in this project, I recognize the importance of writing tests alongside the development process, and I’ll aim to incorporate TDD into my future Django projects to improve test coverage and reliability.

- **Swagger is a game-changer**: Implementing Swagger to document the API was incredibly helpful.


Overall, it was a challenging but rewarding experience. I’m excited to keep learning and applying Django in future projects 😁.
