from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=20, null= False)
    nome_empresa = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('Perfil')
    usuario = models.OneToOneField(User, null=True ,related_name="perfil", on_delete= models.CASCADE)
    
    
    @property
    def email(self):
        return self.usuario.email

    def __str__(self):
        return self.nome

    def convite_a_si_mesmo(self, perfil):
        return self == perfil

    
    def desfazer(self, perfil):
        self.contatos.remove(perfil)
        perfil.contatos.remove(self)

    def pode_convidar(self, perfil):
        nao_pode = self.convite_a_si_mesmo(perfil) or self.ja_eh_contato(perfil) or self.ja_possui_convite(perfil)
        return not nao_pode

    def ja_eh_contato(self, perfil):
        return self.contatos.filter(id = perfil.id).exists()

    def ja_possui_convite(self, perfil):               
        return (Convite.objects.filter(solicitante = self, convidado = perfil).exists() or
                Convite.objects.filter(solicitante = perfil, convidado = self).exists()   )

    def convidar(self, perfil_convidado):
        if self.pode_convidar(perfil_convidado):
            convite = Convite(solicitante=self,convidado = perfil_convidado)
            convite.save()


class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil,on_delete=models.CASCADE,related_name='convites_feitos' )
    convidado = models.ForeignKey(Perfil, on_delete= models.CASCADE, related_name='convites_recebidos')

    def aceitar(self):        
        self.solicitante.contatos.add(self.convidado)
        self.convidado.contatos.add(self.solicitante)
        self.delete()
    
    
    def recusar(self):        
        self.delete()