from django.db import models

from organization.models import Organization

# Create your models here.

class Transaction(models.Model):
     seller = models.ForeignKey('Organization', on_delete=models.CASCADE)
     buyer = models.ForeignKey('Organization', on_delete=models.CASCADE)
     broker = models.ForeignKey('Organization', on_delete=models.CASCADE)
     date = models.DateField()
     quantity = models.IntegerField()
     weight = models.IntegerField()
     rate = models.IntegerField()
     brokerage_rate = models.IntegerField()