# Generated by Django 4.2.5 on 2023-09-05 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=32)),
                ('rg', models.CharField(max_length=9)),
                ('cpf', models.CharField(max_length=1)),
                ('data_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_curso', models.CharField(max_length=10)),
                ('descricao', models.CharField(max_length=100)),
                ('nivel', models.CharField(choices=[('B', 'Básico'), ('I', 'Itermediario'), ('A', 'Avançado')], default='B', max_length=1)),
            ],
        ),
    ]
