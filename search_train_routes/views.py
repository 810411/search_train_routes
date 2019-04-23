from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .forms import UserLoginForm

# Create your views here.


def login_view(request):
    form = UserLoginForm(request.POST or None)
    next_ = request.GET.get('next')

    if form.is_valid():
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()

        user = authenticate(username=username, password=password)

        login(request, user=user)
        next_post = request.POST.get('next')
        redirect_path = next_ or next_post or '/'

        return redirect(redirect_path)

    context = {'form': form}

    return render(request, 'registration/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')
