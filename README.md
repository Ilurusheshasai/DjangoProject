# DjangoProject
Learning Django a Sample project.

This Django project aims to create a robust system with features
for user signup, login, and profile management.

It includes functionalities such as user registration, user data
retrieval, updating user details, and deleting user accounts.

The project utilises Django's built-in features for model creation,
views implementation, URL routing, and template rendering to
achieve seamless user interaction and data management.

Additionally, thorough testing with Postman ensures the
reliability and functionality of the CRUD operations.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Pre-task:
    Created a git repo in github and cloned it locally.
    git clone repo

    Advantage: Now, I dont have to add git remote the main branch from github is what I have now in my local.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Task1: 
    Requirements:
        1) Create Virtual environment.
            python -m venv DjangoAssignment

        2) Install required packages.
            pip install django

        3) Create a New Django Project: Login System
            django-admin startproject LoginSystem       ## To create a project

        4) Create a New Django Application: “Loginify”
            cd LoginSystem
            python manage.py startapp Loginify          ## To create app "Lofinify"

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Now that we have made this small but important change lets commit it
    cd ../
    Now lets create a .gitignore file to add content that you doesnt want git to track.
    once done 
    git status --> you should see changes you made
    git add .  --> the changes will be added to staging area
    git commit -m "Describe what you have done in this commit"
    I am planning to push this later to the remote.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Task 2:
        1. Create Views -> 
            - To handle login functionality
            - To return simple HTTP response

            This file basically contains code that defines what should happen when a user wants to see a view of our application defined in Urls.py. 
            
            projectfolder/applicationfolder/*.py

        2. Define Urls
            - To link urls to the above views

Important: In the loginify folder we create or edit url.py and views.py.

In Django the request first go to the project and then the application.
So we must say somewhere to Django that we have few URL's in out application, we do that by creating or editing the urls.py in 
projectfolder/projectfolder/urls.py
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


