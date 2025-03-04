from django import forms
from django.contrib.auth.models import User
from . import models


class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario',) # excluímos esse campo pois não queremos que o usuário escolha um user, essa informação será preenchida automaticamente.

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')

# Aqui faremos validações do user.
    def clean(self):
        data = self.data
        cleaned = self.cleaned_data
