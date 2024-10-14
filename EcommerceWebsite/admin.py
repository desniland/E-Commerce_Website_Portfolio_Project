from django.contrib import admin
from .models import Item, OrderItem, Order

#Django Administration
class itemAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "photo"]

#Make app modifiable
admin.site.register(Item, itemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
