from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # Renomeando a função para evitar conflito

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        print(username)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  # Usando a função renomeada
            return redirect('home')

    return render(request, 'login.html')
