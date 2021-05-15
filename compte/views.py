from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .form import CreerUtilisateur
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def inscription(request):
    form = CreerUtilisateur()
    if request.method == 'POST':
        form = CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Compte crée avec succes'+user)
            return redirect('compte:acces')
    context = {'form': form}
    return render(request, 'compte/inscription.html', context)


def acces(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print('---------1111')
        print('ZEEEEEEEEE', user)
        if user is not None:
            print('22222222222')
            login(request, user)
            return redirect('produit:home')
        else:
            messages.info(request, 'ereur de mot de passe')

    return render(request, 'compte/acces.html', context)


def logout_user(request):

    logout(request)
    return redirect('compte:acces')
