from django.urls import path
from crawler import views

app_name = "crawler"

urlpatterns = [
    path('', views.index, name='index'),
    path('impressora_adicionar/', views.impressora_adicionar, name='impressora_adicionar'),
]
