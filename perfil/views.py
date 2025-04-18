from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
import copy
from django.contrib.auth import authenticate, login, logout

from . import forms
from . import models

# Create your views here.

class BasePerfil(View):
    template_name = 'perfil/criar.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        self.carrinho = copy.deepcopy(self.request.session.get('carrinho', {}))
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
                    data= self.request.POST or None,
                    instance= self.perfil
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

        self.userform = self.contexto['userform']
        self.perfilform = self.contexto['perfilform']

        if self.request.user.is_authenticated:
            self.template_name = 'perfil/atualizar.html'

        self.renderizar = render(self.request, self.template_name, self.contexto)


    def get(self, *args, **kwargs):
        return self.renderizar

class Criar(BasePerfil):
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.perfilform.is_valid():
            return self.renderizar

        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')

        # Usuário Logado.
        if self.request.user.is_authenticated:
            usuario = get_object_or_404(User, username=self.request.user.username) #type:ignore

            usuario.username = username

            if password:
                usuario.set_password(password)
            
            usuario.email = email
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.save()

            messages.success(
                self.request,
                'Você atualizou seu cadastro com sucesso.')

            if not self.perfil: # Aqui é pra caso o perfil de algum usuário seja excluído na área adm. Daí aqui recria ele.
                self.perfilform.cleaned_data['usuario'] = usuario
                perfil = models.Perfil(**self.perfilform.cleaned_data)
                perfil.save()
            else:
                perfil = self.perfilform.save(commit=False)
                perfil.usuario = usuario
                perfil.save()


        # Usuário Não Logado.
        else:
            usuario = self.userform.save(commit=False)
            usuario.set_password(password)
            usuario.save()

            perfil = self.perfilform.save(commit=False)
            perfil.usuario = usuario
            perfil.save()

            messages.success(
                self.request,
                'Seu cadastro foi realizado com sucesso.')

        if password:
            autentica = authenticate(
                self.request,
                username= usuario,
                password=password
            )
            
            if autentica:
                login(self.request, user=usuario)



        self.request.session['carrinho'] = self.carrinho
        self.request.session.save()


        return redirect('perfil:criar')

class Atualizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Atualizar')

class Login(View):
    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        print(username, '__', password)

        if not username or not password:
            messages.error(
                self.request,
                'Usuário ou senha inválido.'
            )
            return redirect('perfil:criar')

        usuario = authenticate(
                    self.request, 
                    username=username, 
                    password=password)
        
        if not usuario:
            messages.error(
                self.request,
                'Usuário ou senha inválido.'
            )
            return redirect('perfil:criar')
        
        login(self.request, user=usuario)
        messages.success(
            self.request,
            'Login feito com sucesso.'
        )

        return redirect('produto:lista')

class Logout(View):
    def get(self, *args, **kwargs):
        
        carrinho = copy.deepcopy(self.request.session.get('carrinho'))

        logout(self.request)

        self.request.session['carrinho'] = carrinho
        self.request.session.save()

        return redirect('produto:lista')