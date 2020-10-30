from django.shortcuts import render
from django.views.generic.base import View
from perfis.views import get_perfil_logado
class Timeline(View):
    template_name='timeline.html'

    def get(self, request):

        context = {'perfil_logado': get_perfil_logado(request)}
        
        return render(request, self.template_name, context)
    
    
    def post(self, request):
        return render(request, self.template_name, {})

