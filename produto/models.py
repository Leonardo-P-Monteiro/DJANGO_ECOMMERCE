from django.db import models
from utils.image import resize_image

# Create your models here.

class Produto(models.Model):

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='produto_imagens/%Y/%m/', blank=True,
                               null=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField()
    preco_marketing_promocional = models.FloatField(default=0)
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variáveis'),
            ('S', 'Simples'),
        )
    )

    def save(self, *args, **kwargs):
        
        imagem_nome_atual = self.imagem.name
        imagem_mudou = False

        super_save = super().save(*args, **kwargs)

        if self.imagem:
            imagem_mudou = imagem_nome_atual != self.imagem.name
        
        if imagem_mudou:
            print('Redimensionou.')
            resize_image(self.imagem, 800)

        return super_save

    def __str__(self):
        return self.nome

class Variacao(models.Model):

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'

    nome = models.CharField(max_length=255, blank=True, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome

