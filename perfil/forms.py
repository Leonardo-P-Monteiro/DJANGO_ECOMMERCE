from django import forms
from django.contrib.auth.models import User
from . import models


class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario',) # excluímos esse campo pois não queremos que o usuário escolha um user, essa informação será preenchida automaticamente.

class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label= 'Senha'
    )

    password_2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label= 'Confirmação de senha'
    )

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.usuario = usuario


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 
                'password_2', 'email')

    # Aqui faremos validações do user.
    def clean(self):
        data = self.data
        cleaned = self.cleaned_data
        validation_erros_msg = {}

        # Pegando os dados do formulário.
        usuario_data = cleaned.get('username')
        email_data = cleaned.get('email')
        password_data = cleaned.get('password')
        password_2_data = cleaned.get('password_2')

        # Buscando o usuário e email no banco de dados pra ver se já existe.
        usuario_db = User.objects.filter(username=usuario_data).first()
        email_db = User.objects.filter(email=email_data).first()

        error_msg_user_exist = 'Usuário já existe.'
        error_msg_email_exist = 'E-mail já existe.'
        error_msg_pass_match = 'As senhas não coincidem.'
        error_msg_pass_short = 'Sua senha precisa ser maior ou igual a 6 caracteres.'

        # PROCESSAMENTO PARA USUÁRIOS LOGADOS: ATUALIZAR
        if self.usuario:
            if usuario_db:
                if usuario_data != usuario_db.username: #type: ignore
                    validation_erros_msg['username'] = error_msg_user_exist

            if email_data:
                if email_data == email_db:
                    validation_erros_msg['email'] = error_msg_email_exist

            if password_data:
                if password_data != password_2_data:
                    validation_erros_msg['password'] = error_msg_pass_match
                    validation_erros_msg['password_2'] = error_msg_pass_match
            
                if len(password_data) < 6: #type: ignore # Aqui estava dando erro de tipagem mas o script está rodando corretamente.
                    validation_erros_msg['password'] = error_msg_pass_short

        # PROCESSAMENTO PARA USUÁRIO NÃO LOGADOS: CRIAR
        else:
            print('\n Não Logado \n')
            

        if validation_erros_msg:
            raise forms.ValidationError(validation_erros_msg)