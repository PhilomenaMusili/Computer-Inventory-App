from django.db import models
from datetime import datetime, date
# Create your models here.

class Computer(models.Model):
    computer_name = models.CharField(max_length=30, blank=True)
    IP_address = models.CharField(max_length=30, blank=True)
    MAC_address = models.CharField(max_length=30, blank=True)
    os_choice = (
            ('Windows 11', 'Windows 11'),
            ('Windows 10', 'Windows 10'),
            ('Windows 8', 'Windows 8'),
            ('Linux', 'Linux'),
        )
    operating_system = models.CharField(max_length=30, blank=True, null=True, choices=os_choice)

    users_name = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)
    purchase_date=models.DateField("Purchase Date(mm/dd/2023)",auto_now_add=False, auto_now=False, blank=True, null=True)
    timestamp=models.DateField(auto_now_add=True, auto_now=False, blank=True)

def __unicode__(self):
    return self.IP_address + ' ' + self.computer_name