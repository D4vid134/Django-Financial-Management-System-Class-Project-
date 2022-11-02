from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    age = models.IntegerField(null = True)
    address = models.CharField(max_length=250)
    sex = models.CharField(max_length=50)
    occupation = models.CharField(max_length=250)
    
class Agent(models.Model):
    age = models.IntegerField()
    firm = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    fees = models.DecimalField(max_digits = 2, decimal_places = 2)
    
    def __str__(self):
        return self.name
    
class Stock(models.Model):
    name = models.CharField(max_length=250, null=False, primary_key = True)
    abbreviation = models.CharField(max_length=50)
    dayHigh = models.DecimalField(max_digits = 5, decimal_places = 2)
    dayLow = models.DecimalField(max_digits = 5, decimal_places = 2)
    close = models.DecimalField(max_digits = 5, decimal_places = 2)
    open = models.DecimalField(max_digits = 5, decimal_places = 2)
    volume = models.IntegerField()
    prevClose = models.DecimalField(max_digits = 5, decimal_places = 2)
    
    @property
    def percentChange(self):
        result = ((self.close - self.prevClose) / self.prevClose) * 100
        return round(result, 2)
    
    def __str__(self):
        return self.abbreviation
    
class UserStock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, null = True)
    shares = models.DecimalField(max_digits = 6, decimal_places = 3, default = 0)
    
    def __str__(self):
        return self.stock.name
    
class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null = True)
    address = models.CharField(max_length=250)
    price = models.DecimalField(max_digits = 11, decimal_places = 2)
    selling = models.BooleanField(default = False)
    
    def __str__(self):
        return self.address
    
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller', null = True)
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10)
    itemType = models.CharField(max_length=250, null = False)
    price = models.DecimalField(max_digits = 11, decimal_places = 2)
    
    def __str__(self):
        return self.user.username + " " + self.itemType + " $" + str(self.price)

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=False)
    price = models.DecimalField(max_digits = 7, decimal_places = 2)
    selling = models.BooleanField(default = False)
    
    def __str__(self):
        return self.name

