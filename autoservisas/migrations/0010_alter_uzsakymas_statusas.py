# Generated by Django 4.2.7 on 2023-11-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0009_uzsakymas_statusas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uzsakymas',
            name='statusas',
            field=models.CharField(choices=[('l', 'Laukiama automobilio'), ('a', 'Automobiilis tvarkomas'), ('u', 'Užsakymas atliktas'), ('x', 'Užsakymas atšauktas')], default='l', help_text='Statusas', max_length=1),
        ),
    ]
