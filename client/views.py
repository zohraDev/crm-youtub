from django.shortcuts import render
# from django.http import HttpResponse
from .models import Client
from commande.filters import CommandeFilter
from django.contrib.auth.decorators import login_required


@login_required(login_url='compte:acces')
def list_client(request, pk):
    client = Client.objects.get(id=pk)
    commandes = client.commande_set.all()
    commande_count = commandes.count()
    myFilter = CommandeFilter(request.GET, request=commandes)
    commandes = myFilter.qs
    print(commandes)

    context = {'client': client,
               'commandes': commandes,
               'commande_count': commande_count,
               'myFilter': myFilter,
               }

    return render(request, 'client/client.html', context)
