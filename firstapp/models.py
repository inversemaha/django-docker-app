from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    reservation_time = models.DateTimeField(auto_now=True)
    comments = models.CharField(max_length=1000)

    def __str__(self):
        formatted_time = self.reservation_time.strftime("%d-%m-%Y %I:%M %p")
        return f"{self.first_name} {self.last_name} - {self.guest_count} guests at {formatted_time}"