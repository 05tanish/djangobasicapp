from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")

# Logout
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')
def profile_view(request):
    return render(request, 'profile.html')
# Signup
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'signup.html')

        User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')

    return render(request, 'signup.html')


# Home
def home(request):
    return render(request, 'home.html')

# Projects
def todo(request):
    return render(request, 'projects/todo.html')

def cursor(request):
    return render(request, 'projects/cursor.html')

def calculator(request):
    return render(request, 'projects/calculator.html')

def musicplayer(request):
    return render(request, 'projects/musicplayer.html')

def weather(request):
    return render(request, 'projects/weather.html')

def expensetracker(request):
    return render(request, 'projects/expensetracker.html')

def passwordgenerator(request):
    return render(request, 'projects/passwordgenerator.html')

def colourchange(request):
    return render(request, 'projects/colourchange.html')
# Navbar Page
def navbar(request):
    return render(request, 'tweetproject/navbar.html')



# Contact Page
def contact(request):
    if request.method == 'POST':
        # Handle contact form
        pass
    return render(request, 'contact.html')
