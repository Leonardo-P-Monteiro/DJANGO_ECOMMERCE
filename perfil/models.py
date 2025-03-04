from django.db import models
from django.contrib.auth.models import User
from utils.validacpf import valida_cpf
from django.forms import ValidationError
import re # Estude sobre elas (expressões regulares), ainda não fizemos um estudo a respeito.

# Create your models here.

"""
    PerfilUsuario
        user - FK user (ou OneToOne)
        idade - Int
        data_nascimento - Date
        cpf - char
        endereco - char
        numero - char
        complemento - char
        bairro - char
        cep - Char
        cidade - char
        estado - Choices
"""

class Perfil(models.Model):

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    usuario = models.OneToOneField(User,
                             on_delete=models.CASCADE,
                             verbose_name='Usuário')
    idade = models.PositiveIntegerField()
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
    endereco = models.CharField(max_length=50, verbose_name='Endereço')
    numero = models.CharField(max_length=5, verbose_name='Número')
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=8, verbose_name='CEP')
    cidade = models.CharField(max_length=30)
    estado = models.CharField(
        max_length=2,
        default='CE',
        choices= (
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )

    def __str__(self) -> str:
        return f'{self.usuario.first_name} {self.usuario.last_name}'
    
    def clean(self):

        erro_mensagens = {}

        if not valida_cpf(self.cpf):
            erro_mensagens['cpf'] = 'CPF inválido.'
        
        if re.search(r'[^0-9]', self.cep) or len(self.cep)<8:
            erro_mensagens['cep'] = 'CEP inválido.'

        if erro_mensagens:
           raise ValidationError(erro_mensagens)

        return super().clean()