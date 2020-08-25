from django.contrib import admin

# Register your models here.
from crud_app.models import Brand, Product

admin.site.register(Brand)
admin.site.register(Product)
