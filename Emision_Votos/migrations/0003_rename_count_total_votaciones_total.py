# Generated by Django 4.1.2 on 2022-10-08 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Emision_Votos', '0002_votaciones_count_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='votaciones',
            old_name='count_total',
            new_name='total',
        ),
    ]
