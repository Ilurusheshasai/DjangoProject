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

How to verify:
    run this command from the project root:
        python manage.py runserver
    you should be able to access the server at 127.0.0.1:8000
    Attach urls at the end of this base like "http://127.0.0.1:8000/hello/" to gain access to those views.

Note: Login fails as we didn't define any models
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Task 3: Define models, implement views, and set up URLs and templates in
Loginify.

So, Now we define the user model
Django also provides us with UI to see our models. but to this model in UI we need to link it up to the admin page.

We have to make migrations and migrate to see the changes finally.

We need to access signup and login pages and landing page we create a folder called template in loginify, and add these html files there.

in application loginify, add the related views and urls in views.py and urls.py

now commit these changes and sigup on console

still after this step you will not be able to login to django ui, lets do that in next step.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Task 4: MODELS & ADMIN

    1. Setup superuser
        python manage.py createsuperuser 

        configure the details asked.

    2. Access admin page at 127.0.0.1:8000/admin
    3. Getting familiar with django Shell
        - Create new user instance
            new_user = UserDetails.objects.create(username="example_user", email="user@example.com", password="example123")
            
            obj = YourModel.objects.create(field1=value1, field2=value2)


        - Retrieve all Users
            all_users = UserDetails.objects.all()


        - Get a user
            user_by_name = UserDetails.objects.get(username=username)
            queryset = YourModel.objects.filter(field1=value1)


        - Update a user
            obj.field1 = new_value
            obj.save()


        - Delete a user
            username_to_delete= “john”
            user_to_delete =
            User.objects.get(username=username_to_delete)
            obj.delete()
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Task 5:

    1. create views in views.py
    2. Link in urls.py
    3. No need to do anything in login systems urls.py as we have already linked this application endpoints previously.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
