from django.db import models
from perfis.models import Perfil

class Postagem(models.Model):
    texto = models.CharField(max_length=255, null=False)
    data_postagem = models.DateTimeField(auto_now_add=True, blank=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='Postagens')
    
    def __str__(self):
        return self.texto



