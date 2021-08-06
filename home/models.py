from django.conf import settings
from django.db import models


class Home(models.Model):
    "Generated Model"
    distance = models.FloatField()
    price = models.DecimalField(
        max_digits=30,
        decimal_places=10,
    )
    status = models.TextField()
