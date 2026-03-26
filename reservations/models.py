from django.db import models
import string
import random

def generate_confirmation_number():
    length = 8
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

class Reservation(models.Model):
    confirmation_number = models.CharField(max_length=20, unique=True, default=generate_confirmation_number, primary_key=True)
    hotel_name = models.CharField(max_length=255)
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self):
        return self.confirmation_number

class Guest(models.Model):
    reservation = models.ForeignKey(Reservation, related_name='guests_list', on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.guest_name
