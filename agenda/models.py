from django.db import models

# Create your models here.


class MinhaAgenda(models.Model):
    descricao = models.CharField(max_length=255)
    data = models.DateField()
    horario = models.TimeField()