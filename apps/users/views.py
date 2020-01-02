from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SingUpForm, LoginForm, User
from django.contrib.auth.views import LoginView


class LoginPage(LoginView):
    template_name = 'users/login.html'
    authentication_form = LoginForm


# def login_page(request):
#     if request.method == 'POST':
#         login_form = LoginForm(request.POST)
#         if login_form.is_valid():
#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']
#
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user=user)
#                 return redirect('index')
#
#     else:
#         login_form = LoginForm()
#
#     context = {
#         'form': login_form
#     }
#     return render(request, 'users/login.html', context=context)


def logout_page(request):
    logout(request)
    return redirect('index')


def sing_up_page(request):
    if request.method == 'POST':
        sing_up_form = SingUpForm(request.POST)
        if sing_up_form.is_valid():
            username = sing_up_form.cleaned_data['username']
            password = sing_up_form.cleaned_data['password']
            email = sing_up_form.cleaned_data['email']

            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            login(request, user=user)
            return redirect('index')

    else:
        sing_up_form = SingUpForm()

    context = {
        'form': sing_up_form
    }

    return render(request, 'users/sing_up.html', context=context)
