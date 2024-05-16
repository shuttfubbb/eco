from django.contrib import admin
from .models import ShipmentInfo, Transaction, Carriers, Shipment
# Register your models here.
admin.site.register(ShipmentInfo)
admin.site.register(Transaction)
admin.site.register(Carriers)
admin.site.register(Shipment)
