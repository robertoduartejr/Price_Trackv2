# Generated by Django 4.1 on 2022-08-30 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import track.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', track.models.NameField(max_length=100)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('url', models.URLField(max_length=500)),
                ('site', models.CharField(choices=[('Mercado Livre', 'Mercado Livre'), ('Amazon', 'Amazon'), ('Magazine Luiza', 'Magazine Luiza'), ('Americanas', 'Americanas')], default='Mercado Livre', max_length=14)),
                ('desired_price', models.FloatField(default=10.0)),
                ('prices', models.JSONField(null=True)),
                ('ativa', models.BooleanField(default=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
