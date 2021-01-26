from django.urls import path
from . import views

app_name = 'discount'

urlpatterns = [
    path('', views.home, name='home')
]
