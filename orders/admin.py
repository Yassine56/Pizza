from django.contrib import admin
from .models import Toppings, RegularPizza, ScicilianPizza, Subs, DinnerPlate, Pasta, Salads, Order
# Register your models here.

admin.site.register(Toppings)
admin.site.register(Subs)
admin.site.register(RegularPizza)
admin.site.register(ScicilianPizza)
admin.site.register(DinnerPlate)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(Order)
