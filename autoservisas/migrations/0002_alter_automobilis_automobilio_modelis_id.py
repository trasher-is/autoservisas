# Generated by Django 4.2.7 on 2023-11-07 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automobilis',
            name='automobilio_modelis_id',
            field=models.ForeignKey(db_column='automobilio_modelis', on_delete=django.db.models.deletion.PROTECT, to='autoservisas.automobilio_modelis', verbose_name='automobilio modelis'),
        ),
    ]
