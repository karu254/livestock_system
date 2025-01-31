from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileUpdateForm
from .models import Profile
from accounts.models import CustomUser

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('dashboard') # Redirect to dashboard after login(correction from home)
#         else:
#             messages.error(request, 'Invalid username or password.')
#     return render(request, 'accounts/login.html')

#trying to fix the login issue
def custom_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Redirect based on role field
            if user.role == "admin":
                return redirect("dashboard_home")  # Admin dashboard
            else:
                return redirect("profile")  # Regular user profile page
        else:
            return render(request, "accounts/login.html", {"error": "Invalid credentials"})

    return render(request, "accounts/login.html")




@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)  # Ensure Profile exists
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, "accounts/profile.html", {"form": form})
