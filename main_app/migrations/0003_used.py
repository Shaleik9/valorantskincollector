# Generated by Django 4.2 on 2023-04-24 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_skin_edition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Used',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Used Date')),
                ('valmap', models.CharField(choices=[('Lotus', 'Lotus'), ('Pearl', 'Pearl'), ('Fracture', 'Fracture'), ('Breeze', 'Breeze'), ('Icebox', 'Icebox'), ('Bind', 'Bind'), ('Haven', 'Haven'), ('Split', 'Split'), ('Ascent', 'Ascent')], default='Lotus', max_length=10)),
                ('skin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.skin')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
