from django.db import models
import jsonfield
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField
from django.utils import timezone
from django.contrib.auth.models import User

class NameField(models.CharField): #function

    def get_prep_value(self, value):
        return str(value).capitalize()

SITE_CHOICES = (
    ('mercado_livre','Mercado Livre'),
    ('amazon','Amazon'),
    ('magazine_luiza','Magazine Luiza'),
    ('americanas','Americanas')
)


class Track(models.Model):
    name = NameField(max_length=100)
    pub_date = models.DateTimeField('date published',default=timezone.now)
    url = models.URLField(max_length=500)
    site = models.CharField(max_length=14,choices=SITE_CHOICES,default='Mercado Livre')
    desired_price = models.FloatField(default=10.0)
    prices = models.JSONField(null=True)
    ativa = models.BooleanField(default=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name