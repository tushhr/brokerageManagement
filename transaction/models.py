from django.db import models

from organization.models import Organization

# Create your models here.

class Item(models.Model):
     name = models.CharField(max_length=100)

     def __str__(self):
         return self.name

class Transaction(models.Model):
     seller = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='seller')
     buyer = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='buyer')
     broker = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='broker')
     date = models.DateField()
     item = models.ForeignKey(Item, on_delete=models.CASCADE)
     quantity = models.IntegerField()
     weight = models.DecimalField(max_digits=100, decimal_places=2)
     rate = models.IntegerField()
     seller_brokerage_rate = models.DecimalField(max_digits=100, decimal_places=2)
     buyer_brokerage_rate = models.DecimalField(max_digits=100, decimal_places=2)

     def __str__(self):
          return self.seller.name + ' sold to ' + self.buyer.name + ' on ' + str(self.date)