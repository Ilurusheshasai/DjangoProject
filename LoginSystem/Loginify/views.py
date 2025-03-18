from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserDetails
from django.contrib import messages

# Test view
def hello_world(request):
    return HttpResponse("Hello, world!")

# Placeholder login view (will build later)
def login_view(request):
    return HttpResponse("This is the login page")

# Signup View
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if email already exists
        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return redirect('signup')

        # Save user
        user = UserDetails(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Signup successful! Please login.')
        return redirect('login')
    
    return render(request, 'signup.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserDetails.objects.get(email=email, password=password)
            messages.success(request, f'Welcome {user.username}! You logged in successfully.')
            return render(request, 'login_success.html', {'user': user})
        except UserDetails.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')

    return render(request, 'login.html')
