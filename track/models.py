from django.db import models
import jsonfield
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

import main.models


def get_default_json():
    return {"data": [["date", "price"]]}

class NameField(models.CharField): #function

    def get_prep_value(self, value):
        return str(value).capitalize()

SITE_CHOICES = (
    ('Mercado Livre','Mercado Livre'),
    ('Amazon','Amazon'),
    ('Magazine Luiza','Magazine Luiza'),
    ('Americanas','Americanas')
)


class Track(models.Model):
    name = NameField(max_length=100)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    url = models.URLField(max_length=500)
    site = models.CharField(max_length=14,choices=SITE_CHOICES)
    desired_price = models.FloatField(default=10.0)
    prices = models.JSONField(null=True, default=get_default_json)
    ativa = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name