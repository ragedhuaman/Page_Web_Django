# Generated by Django 3.2.3 on 2021-05-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
    ]