from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    times = models.CharField(
        max_length=50,
        choices=[
            ('Nenhum', 'Nenhum'),
            ('Sport', 'SPORT CLUB DO RECIFE'),
            ('Santa', 'Santa cruz'),
            ('Nautico', 'Náutico'),
            ('Fortaleza', 'Fortaleza'),
            ('Ceará', 'Ceará'),
            ('Remo', 'Remo'),
            ('paysandu', 'Paysandu'),
            ('vitoria', 'Vitória'),
        ],
        blank=True,
        default='Nenhum'
    )

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name