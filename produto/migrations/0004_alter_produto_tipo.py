# Generated by Django 5.1.6 on 2025-02-15 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_produto_options_alter_variacao_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('V', 'Variável'), ('S', 'Simples')], default='V', max_length=1),
        ),
    ]
