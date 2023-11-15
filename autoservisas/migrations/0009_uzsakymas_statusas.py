# Generated by Django 4.2.7 on 2023-11-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0008_alter_automobilis_automobilio_modelis_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uzsakymas',
            name='statusas',
            field=models.CharField(choices=[('l', 'Laukiama automobilio'), ('a', 'Automobiilis tvarkomas'), ('u', 'Užsakymas atliktas'), ('x', 'Užsakymas atšauktas')], default='a', help_text='Statusas', max_length=1),
        ),
    ]
