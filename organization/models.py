from django.db import models

# Create your models here.
class Organization(models.Model):
    ORG_TYPE = (
        ('BR', 'broker'),
        ('CL', 'client'),
    )

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    brokerage_rate = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    org_type = models.CharField(max_length=2, choices=ORG_TYPE, default='CL')
    bank = models.CharField(max_length=100, null=True, blank=True)
    bank_account = models.IntegerField(null=True, blank=True)
    rtgs_code = models.CharField(max_length=100, null=True, blank=True)
    gst_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name