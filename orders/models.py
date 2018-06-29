from django.db import models

# Create your models here.
class Order(models.Model):
    firstname = models.CharField(max_length=64)
    items = models.CharField(max_length=500)
    price = models.FloatField(null=True, blank=True)
    totalprice = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"{self.firstname}:{self.items}:{self.totalprice}"

class Toppings(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.name}"

class RegularPizza(models.Model):
    kind = models.CharField(max_length=64)
    smallPrice = models.FloatField(null=True, blank=True)
    largePrice = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"{self.kind}"
    #toppings = models.OneToManyField(Toppings, symmetrical=False)

class ScicilianPizza(models.Model):
    kind = models.CharField(max_length=64)
    smallPrice = models.FloatField(null=True, blank=True)
    largePrice = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"{self.kind}"
class Subs(models.Model):
    name = models.CharField(max_length=64)
    smallPrice = models.FloatField(null=True, blank=True)
    largePrice = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"{self.name}"
class DinnerPlate(models.Model):
    name = models.CharField(max_length=64)
    smallPrice = models.FloatField(null=True, blank=True)
    largePrice = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"{self.name}"
class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"{self.name}"
class Salads(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"{self.name}"
