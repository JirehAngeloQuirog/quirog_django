from django.contrib import admin
from .models import Vehicle, Booking

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'vehicle_type', 'price_per_day', 'available')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'vehicle', 'start_date', 'end_date', 'total_price', 'status', 'payment_status')