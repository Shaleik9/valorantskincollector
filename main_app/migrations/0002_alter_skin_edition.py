# Generated by Django 4.2 on 2023-04-24 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skin',
            name='edition',
            field=models.CharField(choices=[('Select', 'Select'), ('Deluxe', 'Deluxe'), ('Premium', 'Premium'), ('Exclusive', 'Exclusive'), ('Ultra', 'Ultra')], default='Select', max_length=15),
        ),
    ]
