from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import HttpRequest, HttpResponse

from . import forms
from . import models

# Create your views here.

class BasePerfil(View):
    template_name = 'perfil/criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs) # Se eu quiser posso passar a "request" pra ele também.
        
        self.perfil = None

        if self.request.user.is_authenticated:
            self.perfil = models.Perfil.objects.\
                filter(usuario=self.request.user).first()
            self.contexto = {
                'userform': forms.UserForm(
                    data= self.request.POST or None, 
                    usuario= self.request.user,
                    instance = self.request.user,
                ),
                'perfilform': forms.PerfilForm(
                    data= self.request.POST or None
                )
            }
        else:            
            self.contexto = {
            'userform': forms.UserForm(
                data= self.request.POST or None
            ),
            'perfilform': forms.PerfilForm(
                data= self.request.POST or None
            )
        }
    
        self.renderizar = render(self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar

class Criar(BasePerfil):
    def post(self, *args, **kwargs):
        return self.renderizar    

class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')

class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')

class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')