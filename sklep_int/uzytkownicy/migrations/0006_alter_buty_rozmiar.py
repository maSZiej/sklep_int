# Generated by Django 3.2.9 on 2023-02-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzytkownicy', '0005_auto_20230221_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buty',
            name='rozmiar',
            field=models.IntegerField(choices=[(38, 'Male 38'), (39, 'Male 39'), (40, 'Srednie 40'), (41, 'Srednie 41'), (42, 'Duze 42'), (43, 'Duze 43')], default=40),
        ),
    ]