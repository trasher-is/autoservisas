# Generated by Django 4.2.7 on 2023-11-15 09:13

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0014_uzsakymas_grazinimo_terminas'),
    ]

    operations = [
        migrations.AddField(
            model_name='automobilis',
            name='aprasymas',
            field=tinymce.models.HTMLField(default=0),
            preserve_default=False,
        ),
    ]