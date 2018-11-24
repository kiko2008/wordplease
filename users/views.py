from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user_in_session, logout as destroy_user_session
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from users.forms import RegisterForm, LoginForm


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Usuario o password incorrectos!')
        else:
            login_user_in_session(request, user)
            return redirect(request.GET.get('next', 'home'))

        form = LoginForm()
        return render(request, 'login.html', {'form': form})


class LogoutView(View):

    def get(self, request):
        destroy_user_session(request)
        return redirect('home')


class LogupView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'logup.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = User()
            new_user.first_name = form.cleaned_data.get('first_name')
            new_user.last_name = form.cleaned_data.get('last_name')
            new_user.username = form.cleaned_data.get('username')
            new_user.email = form.cleaned_data.get('email')
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()
            messages.success(request, 'Usuario creado correctamente!')
            form = RegisterForm()

        return render(request, 'logup.html', {'form': form})
