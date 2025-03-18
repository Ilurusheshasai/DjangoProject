# DjangoProject

## Overview

This Django project focuses on building a user **Login System**. It includes:

- User **Signup**
- User **Login**
- **Profile Management**
- Full **CRUD Operations** (Create, Read, Update, Delete)
- Django Admin Integration
- Postman testing for API endpoints

The project leverages Django’s built-in features such as:

- Model creation
- Views implementation
- URL routing
- Template rendering
- Django Admin UI
- Django Shell operations

---

## Key Features

- User registration & authentication system
- Retrieve, update, delete user details
- Integration with Django Admin panel
- Full CRUD operations exposed as endpoints
- Tested via Postman for reliability

---

## Pre-Task Setup

1. **Created a GitHub repository and cloned it locally:**

```bash
git clone <repo_url>
```

**Advantage:**  
No need to add remote manually. The `main` branch from GitHub is already linked locally.

---

## Task 1: Initial Setup

### Requirements:

1. **Create a virtual environment:**

```bash
python -m venv DjangoAssignment
```

2. **Activate the environment and install Django:**

```bash
pip install django
```

3. **Create a new Django Project:**

```bash
django-admin startproject LoginSystem
```

4. **Create a Django Application:**

```bash
cd LoginSystem
python manage.py startapp Loginify
```

5. **Setup `.gitignore` and Git commits:**

```bash
touch .gitignore
git status
git add .
git commit -m "Initial project setup"
```

---

## Task 2: Views and URLs

1. **Create Views:**

- Handle login functionality
- Return a simple **HTTP response** for testing purposes

```python
# In Loginify/views.py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world!")
```

2. **Define URLs:**

- Map URLs to views both in **Loginify** app and project-level `urls.py`.

---

## Task 3: Models, Views, Templates

1. **Define Models:**

```python
# In Loginify/models.py
from django.db import models

class UserDetails(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=12, blank=True)
```

2. **Migrate the database:**

```bash
python manage.py makemigrations
python manage.py migrate
```

3. **Setup templates (HTML forms for Signup/Login).**

4. **Implement corresponding views and URLs for handling signup & login.**

---

## Task 4: Django Admin & Shell Operations

1. **Create superuser:**

```bash
python manage.py createsuperuser
```

2. **Access Django Admin:**

```
http://127.0.0.1:8000/admin
```

3. **Register `UserDetails` model in `admin.py`.**

4. **Django Shell Operations:**

```python
from Loginify.models import UserDetails

# Create new user
new_user = UserDetails.objects.create(username="example_user", email="user@example.com", password="example123")

# Retrieve all users
all_users = UserDetails.objects.all()

# Get user by username
user_by_name = UserDetails.objects.get(username="example_user")

# Update user
user_by_name.password = "newpassword"
user_by_name.save()

# Delete user
user_by_name.delete()
```

---

## Task 5: CRUD API Implementation

1. **Implemented CRUD Views:**

- **Get all users**
- **Get user by email**
- **Update user details**
- **Delete user by email**

2. **Linked URLs in `Loginify/urls.py`.**

**Note:** No changes required in project-level URLs as app URLs are already included.

---

## Testing:

- All CRUD operations tested using **Postman**.
- CSRF tokens exempted for API testing.
- JSON data is passed in Postman to perform POST/PATCH operations for updating users.

---

## Tech Stack:

- **Django 4+**
- **SQLite** (default DB)
- **HTML/CSS (Templates)**
- **Postman** (for API testing)
- **Git & GitHub**

---

## Future Enhancements:

- Use **Django REST Framework (DRF)** to build cleaner REST APIs
- Add **Token-based Authentication**
- Implement **Sessions & Logout**
- Add **Password Hashing** (currently passwords are plain text, not secure)
- Improve frontend UI (Bootstrap, Tailwind CSS, etc.)

---

## Learning Outcome:

- Complete understanding of Django’s MVT structure
- How models, views, templates, and URLs work together
- Hands-on experience with CRUD operations
- Admin panel integration
- Basic API building and testing process
