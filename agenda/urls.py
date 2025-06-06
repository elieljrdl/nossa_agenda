from django.urls import path
from . import views

urlpatterns = [
    path("minha_agenda/", views.agenda, name="agenda"),
    path('excluir/<int:id>/', views.excluir_compromisso, name='excluir_compromisso'),
    path('adiciona/', views.adiciona_compromisso, name='adiciona_compromisso'),
]