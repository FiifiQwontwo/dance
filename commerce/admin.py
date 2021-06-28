from django.contrib import admin
from .models import *


# Register your models here.

class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class VendorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_of_vendor', 'name_of_shop')}


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(VendorSign, VendorAdmin)
