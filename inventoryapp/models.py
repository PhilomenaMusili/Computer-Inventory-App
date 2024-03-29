from django.db import models
from datetime import datetime, date

class OperatingSystem(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Computer(models.Model):
    computer_name = models.CharField(max_length=30, blank=True)
    IP_address = models.CharField(max_length=30, blank=True)
    MAC_address = models.CharField(max_length=30, blank=True)
    operating_system = models.ManyToManyField(OperatingSystem, blank=True)
    users_name = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)
    purchase_date = models.DateField("Purchase Date (mm/dd/2023)", auto_now_add=False, auto_now=False, blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.computer_name} ({', '.join(os.name for os in self.operating_system.all())})"
class ComputerHistory(models.Model):
     computer_name = models.CharField(max_length=30, blank=True, null=True)
     IP_address = models.CharField(max_length=30, blank=True, null=True)
     MAC_address = models.CharField(max_length=30, blank=True, null=True)
     operating_system = models.ForeignKey(OperatingSystem, blank=True, null=True, on_delete=models.CASCADE)
     users_name = models.CharField(max_length=30, blank=True, null=True)
     location = models.CharField(max_length=30, blank=True, null=True)
     purchase_date = models.DateField("Purchase Date(mm/dd/yyyy)", auto_now_add=False, auto_now=False, blank=True, null=True)
     timestamp = models.DateField(auto_now_add=True, auto_now=False, blank=True, null=True)