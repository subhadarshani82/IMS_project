from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser
from django.contrib import messages
from django.db.utils import IntegrityError

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm_password']
        role = request.POST['role']
        status = 'Approved'
        phone = request.POST['phone']
        address = request.POST['address']

        if password != confirm:
            return render(request, 'register.html', {'error': 'Passwords do not match!'})

        try:
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                role=role,
                status=status,
                phone=phone,
                address=address
            )
            user.save()
            return redirect('login')
        except IntegrityError:
            return render(request, 'register.html', {'error': 'Username or Email already exists!'})
    return render(request, 'register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            if user.status == "Approved":
                login(request, user)
                return redirect('dashboard')  # Redirect to home/dashboard page
            else:
                return render(request, 'login.html', {'error': 'Your account is not approved yet.'})
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
def dashboard(request):
    return render(request,'dashboard.html')