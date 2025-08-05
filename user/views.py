from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return render(request, 'main/home.html')
        else:
            return render(request, 'user/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'user/login.html')

def logout(request):
    return render(request, 'user/login.html')