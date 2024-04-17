from django.db import models

from organization.models import Organization

# Create your models here.

class Transaction(models.Model):
     seller = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='seller')
     buyer = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='buyer')
     broker = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='broker')
     date = models.DateField()
     item = models.CharField(max_length=100)
     quantity = models.IntegerField()
     weight = models.DecimalField(max_digits=100, decimal_places=2)
     rate = models.IntegerField()
     brokerage_rate = models.IntegerField()