from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user_in_session, logout as destroy_user_session
from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):

    def get(self, request):

        return render(request, 'login.html')

    def post(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Usuario o password incorrectos!')
        else:
            login_user_in_session(request, user)
            return redirect(request.GET.get('next', 'home'))

        return render(request, 'login.html')


class LogoutView(View):

    def get(self, request):
        destroy_user_session(request)
        return redirect('home')