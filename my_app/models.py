from django.db import models
from django.utils import timezone


class Weight(models.Model):
    weight = models.CharField(max_length=5)
    date = models.DateTimeField()

    def _str__(self):
        return str(self.weight)

    #def _str__(self):
    #    return str(self.date)    
