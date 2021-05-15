from django.urls import path
from .views import list_commande, ajouter_commande, modifier_commande, supprimer_commande

app_name = 'commande'

urlpatterns = [
    path('', list_commande, name='list_commande'),
    path('ajouter_commande', ajouter_commande, name='ajouter_commande'),
    path('modifier_commande/<int:pk>', modifier_commande, name='modifier_commande'),
    path('supprimer_commande/<int:pk>', supprimer_commande, name='supprimer_commande'),
]
