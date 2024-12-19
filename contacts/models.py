from django.db import models
from datetime import datetime
from listings.models import Listing

# Create your models here.

class Contact(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.CharField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    # User who is logged in should also be able to make inquiry. So making it optional.
    user_id = models.IntegerField(blank=True)
    realtor_email = models.CharField(max_length=100)

def __str__(self):
    return self.name
