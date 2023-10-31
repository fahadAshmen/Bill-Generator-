from django.contrib import admin
from . models import Bill, BillItems

admin.site.register(BillItems)
admin.site.register(Bill)
