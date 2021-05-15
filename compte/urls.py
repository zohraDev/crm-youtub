from django.urls import path
from .views import *


app_name = 'compte'

urlpatterns = [
    path('inscription', inscription, name='inscription'),
    path('acces', acces, name='acces'),
    path('quitter', logout_user, name='quitter'),

]
