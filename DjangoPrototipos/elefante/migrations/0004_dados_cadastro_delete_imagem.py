# Generated by Django 4.1 on 2022-09-23 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elefante', '0003_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='dados_cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Imagem',
        ),
    ]