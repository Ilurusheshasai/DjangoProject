from django.shortcuts import render
from django.http import HttpResponse

# Test view
def hello_world(request):
    return HttpResponse("Hello, world!")

# Placeholder login view (will build later)
def login_view(request):
    return HttpResponse("This is the login page")
