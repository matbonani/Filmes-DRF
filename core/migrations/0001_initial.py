# Generated by Django 3.2 on 2022-03-02 19:22

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('atualizacao', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=False, verbose_name='Ativo')),
                ('filme', models.CharField(max_length=150, unique=True, verbose_name='Nome do Filme')),
            ],
            options={
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('atualizacao', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=False, verbose_name='Ativo')),
                ('username', models.CharField(max_length=105, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('avaliacoes', models.DecimalField(decimal_places=1, max_digits=2, validators=[core.models.valida_nota])),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='core.filme')),
            ],
            options={
                'verbose_name': 'Avaliação',
                'verbose_name_plural': 'Avaliações',
                'unique_together': {('username', 'filme')},
            },
        ),
    ]
