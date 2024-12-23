from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.

def register(request):
    if request.method == 'POST':
        # Get Form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_2 = request.POST['password2']

        # Check if passwords match
        if password == password_2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                # Check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('register')
                else:
                    # Validations passed
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                    )
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'User registered and logged in')
                    # return redirect('index')

                    # Register but redirect to login page for manual login
                    user.save()
                    messages.success(request, 'User registered. Please proceed to log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        # User found
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in succesfully')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'User has been logged out')
        return redirect('index')