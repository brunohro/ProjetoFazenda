# Generated by Django 5.1.6 on 2025-02-06 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fazenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='data_de_cadastro',
            field=models.DateTimeField(),
        ),
    ]
