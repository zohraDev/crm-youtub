from django.forms import ModelForm
from .models import Commande


class CommandeFrom(ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'
