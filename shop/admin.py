from django.contrib import admin
from django.contrib.admin import filters


# Register your models here.

from .models import Cart, Contact, Order, Product

admin.action()


class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'category', 'subCategory')
    search_fields = ("name",)
    list_filter = ("category",)


admin.site.register(Product, productAdmin)
admin.site.register(Contact)
admin.site.register(Cart)
admin.site.register(Order)
