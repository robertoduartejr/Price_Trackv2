# Generated by Django 4.1 on 2022-09-05 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_alter_track_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='prices',
            field=models.JSONField(default={'data': [['date', 'price'], ['September 05, 2022 Monday, 12:10:04', '100']]}, null=True),
        ),
    ]
