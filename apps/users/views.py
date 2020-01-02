from django.shortcuts import render, redirect
from django import forms
from django.forms import widgets
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username')
    password = forms.CharField(max_length=50, label='Password', widget=widgets.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('User with such username does not exist')

        if not user.check_password(cleaned_data['password']):
            raise forms.ValidationError('Password is incorrect')


class SingUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=widgets.PasswordInput)
    confirm_password = forms.CharField(max_length=50, widget=widgets.PasswordInput)
    email = forms.EmailField(max_length=50)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        username = cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError('User with such username already exist')
        except User.DoesNotExist:
            pass

        if len(password) < 4:
            raise forms.ValidationError('Password too short')

        if password != confirm_password:
            raise forms.ValidationError('Password and confirm-password does not match')


def login_page(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user=user)
                return redirect('index')

    else:
        login_form = LoginForm()

    context = {
        'form': login_form
    }
    return render(request, 'users/login.html', context=context)


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
