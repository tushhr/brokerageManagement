from django.db import models

# Create your models here.
class Organization(models.Model):
    ORG_TYPE = (
        ('0', 'broker'),
        ('1', 'client'),
    )

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField()
    org_type = models.CharField(max_length=1, choices=ORG_TYPE, default='0')
    bank = models.CharField(max_length=100)
    bank_account = models.IntegerField()
    rtgs_code = models.CharField(max_length=100)
    gst_number = models.CharField(max_length=100)