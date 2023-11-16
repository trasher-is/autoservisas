# Generated by Django 4.2.7 on 2023-11-16 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autoservisas', '0016_alter_uzsakymas_automobilis_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uzsakymas',
            name='automobilis_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auto_statusas', to='autoservisas.automobilis', verbose_name='Informacija'),
        ),
        migrations.CreateModel(
            name='UzsakymasReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('atsiliepimo_tekstas', models.TextField(max_length=2000, verbose_name='Atsiliepimas')),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('uzsakymas_review_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='autoservisas.uzsakymas')),
            ],
            options={
                'verbose_name': 'Atsiliepimas',
                'verbose_name_plural': 'Atsiliepimai',
                'ordering': ['-date_created'],
            },
        ),
    ]