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




from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth.decorators import login_required


def add_product(request):
    categories = Category.objects.all()

    if request.method == "POST":
        name = request.POST['name']
        description = request.POST.get('description', '')
        price = request.POST['price']
        quantity = request.POST['quantity']
        category_id = request.POST['category']
        image = request.FILES.get('image')
        

        try:
            category = Category.objects.get(id=category_id)
            product = Product.objects.create(
                name=name,
                description=description,
                price=price,
                quantity=quantity,
                category=category,
                image=image,
                created_by=request.user,
            )
            return render(request, 'add_product.html', {
                'message': 'Product added successfully!',
                'categories': categories
            })
        except Exception as e:
            return render(request, 'add_product.html', {
                'error': f"Failed to add product: {e}",
                'categories': categories
            })

    return render(request, 'add_product.html', {'categories': categories})

def list_products(request):
    
    products = Product.objects.all()
    return render(request, 'list_products.html', {'products': products})