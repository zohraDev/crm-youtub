from .models import Commande
import django_filters


class CommandeFilter(django_filters.FilterSet):
    class Meta:
        model = Commande
        #fields = ['produit', 'status']
        fields = '__all__'
        exclude = ['created_at', 'client']