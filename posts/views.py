from django.shortcuts import render, redirect
from django.views.generic.base import View
from perfis.views import get_perfil_logado
from posts.models import Postagem 
from posts.forms import PostagemForm 
from django.contrib.auth.decorators import login_required


@login_required
def timeline(request):
    template_name='timeline.html'
    user = get_perfil_logado(request)
    form = PostagemForm()
    friends = user.contatos.all()
    postagens = Postagem.objects.filter(perfil__in=friends).order_by('data_postagem').reverse()
    context = {'perfil_logado': user,'form':form, 'posts':postagens}
    if request.method=='POST':
        form = PostagemForm(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            post = Postagem(texto=data_form['texto'], perfil=context['perfil_logado'])
            post.save()
            return redirect('/')
    return render(request, template_name, context)