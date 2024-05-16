from django.db import models

class Fullname(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    def __str__(self):
        return self.fname + " " + self.lname

class Address(models.Model):
    nohouse = models.CharField(max_length=20)
    street = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.nohouse + " " + self.street + " " + self.district + " " + self.city
    
class Account(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username
    

class User(models.Model):
    id = models.CharField(max_length=7, primary_key=True)
    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    position = models.IntegerField()
    
    def __str__(self):
        return self.fullname.__str__()