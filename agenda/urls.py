from django.urls import path
from . import views

urlpatterns = [
    path("minha_agenda/", views.agenda, name="agenda"),
    path("inserir_compromisso", views.inserir_compromisso, name="inserir"),
]