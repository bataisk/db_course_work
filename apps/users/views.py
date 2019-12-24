from django.shortcuts import render


def login_page(request):
    return render(request, 'users/login.html')


def sing_up_page(request):
    return render(request, 'users/sing_up.html')
