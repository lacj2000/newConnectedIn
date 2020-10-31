from django.forms import ModelForm
from posts.models import Postagem


class PostagemForm(ModelForm):
    class Meta:
        model = Postagem
        fields = ['texto']