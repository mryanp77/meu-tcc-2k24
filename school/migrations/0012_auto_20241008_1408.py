# Generated by Django 3.0.5 on 2024-10-08 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20200508_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='cl',
            field=models.CharField(choices=[('1º Ano A', '1º Ano A'), ('2º Ano A', '2º Ano A'), ('3º Ano A', '3º Ano A'), ('1º Ano B', '1º Ano B'), ('2º Ano B', '2º Ano B'), ('3º Ano B', '3º Ano B'), ('Subsequente 1', 'Subsequente 1'), ('Subsequente 2', 'Subsequente 2'), ('Subsequente 3', 'Subsequente 3'), ('Subsequente 4', 'Subsequente 4')], default='1º Ano A', max_length=15),
        ),
    ]
