# Generated by Django 4.2.7 on 2023-11-08 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0006_alter_automobiliomodelis_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uzsakymoeilute',
            name='uzsakymas_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autoservisas.uzsakymas', verbose_name='Užsakymo informacija'),
        ),
    ]
