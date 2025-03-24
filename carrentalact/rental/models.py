from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(
        max_length=50, 
        choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Luxury', 'Luxury')]
    )
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('Complete', 'Complete'), ('Cancelled', 'Cancelled')], default="Complete")
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"Booking {self.id} - {self.user.username}"