from django.conf.urls import url
from General.views import *

app_name = 'home'

urlpatterns = [
	url('',Inicio, name='Inicio'),
]
