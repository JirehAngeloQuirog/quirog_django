from django.shortcuts import render
from django.db.models import Avg
from .models import Booking

def successful_bookings():
    return Booking.objects.filter(payment_status='paid')

def failed_bookings():
    return Booking.objects.filter(payment_status='failed')

def average_sales():
    return Booking.objects.filter(payment_status='paid').aggregate(Avg('total_price'))