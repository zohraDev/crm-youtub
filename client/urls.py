from django.urls import path
from .views import list_client

app_name = 'client'

urlpatterns = [

    path('<str:pk>/', list_client, name='list_client')

]
