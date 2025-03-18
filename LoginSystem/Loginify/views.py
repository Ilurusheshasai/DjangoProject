from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from .models import UserDetails
from django.contrib import messages
import json

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

# Get all users
def get_all_users(request):
    users = UserDetails.objects.all().values()
    return JsonResponse(list(users), safe=False)

# Get single user by email
def get_user_by_email(request, email):
    try:
        user = UserDetails.objects.get(email=email)
        user_data = {
            'username': user.username,
            'email': user.email,
            'password': user.password
        }
        return JsonResponse(user_data)
    except UserDetails.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

# Update user details
@csrf_exempt
def update_user(request, email):
    if request.method in ['POST', 'PATCH']:
        try:
            user = UserDetails.objects.get(email=email)

            try:
                data = json.loads(request.body.decode('utf-8'))
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON data'}, status=400)
            
            username = data.get('username', user.username)
            password = data.get('password', user.password)

            # Update fields using queryset's update
            UserDetails.objects.filter(email=email).update(username=username, password=password)

            return JsonResponse({'message': 'User updated successfully'})
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

# Delete user by email
@csrf_exempt
def delete_user(request, email):
    if request.method == 'POST':
        try:
            user = UserDetails.objects.get(email=email)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=400)