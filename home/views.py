from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Função para encaminhar o usuario para a home
def home(request):
     return render(request, 'home/home.html')

# Função para logout e encaminhar para a home
def my_logout(request):
    logout(request)
    return redirect('home')
