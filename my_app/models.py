from django.db import models
from datetime import datetime


class Weight(models.Model):
    weight = models.CharField(max_length=5)
    date = models.DateTimeField(default=datetime.now())

    def _str__(self):
        return self.weight
