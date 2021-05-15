from django.shortcuts import render, redirect
from .form import CommandeFrom
from .models import Commande
from django.contrib.auth.decorators import login_required


@login_required(login_url='compte:acces')
def list_commande(request):
    return render(request, 'commande/commande.html')


@login_required(login_url='compte:acces')
def ajouter_commande(request):
    form = CommandeFrom()
    if request.method == 'POST':
        form = CommandeFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'commande/ajouter_commande.html', context)


@login_required(login_url='compte:acces')
def modifier_commande(request, pk):
    commande = Commande.objects.get(id=pk)
    form = CommandeFrom(instance=commande)
    if request.method == 'POST':
        form = CommandeFrom(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'commande/ajouter_commande.html', context)


@login_required(login_url='compte:acces')
def supprimer_commande(request, pk):
    command = Commande.objects.get(id=pk)
    if request.method =='POST':
        command.delete()
        return redirect('/')
    context = {
        'item': command,
    }

    return render(request, 'commande/supprimer_commande.html', context)
