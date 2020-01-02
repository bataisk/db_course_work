from django import forms
from django.forms import widgets
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