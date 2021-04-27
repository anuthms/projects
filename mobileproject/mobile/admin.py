from django.contrib import admin


# Register your models here.
from .models import Mobile,Brands,Order
admin.site.register(Brands)
admin.site.register(Mobile)
admin.site.register(Order)

