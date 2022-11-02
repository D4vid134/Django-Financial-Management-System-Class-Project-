from django.contrib import admin
from .models import Agent, UserStock, Property, Transaction, Stock, User, Item

# Register your models here.


admin.site.register(Agent)
admin.site.register(UserStock)
admin.site.register(Property)
admin.site.register(Transaction)
admin.site.register(Stock)
admin.site.register(User)
admin.site.register(Item)



