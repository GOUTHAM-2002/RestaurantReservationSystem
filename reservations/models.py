from django.db import models
from datetime import date

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Membership(models.Model):
    name = models.CharField(max_length=100)
    benefits = models.TextField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    memberships = models.ManyToManyField(Membership,blank=True)

    def __str__(self):
        return self.name

class ReservationManager(models.Manager):
    def upcoming_reservations(self):
        return self.filter(date__gte=date.today())

class Reservations(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.PositiveSmallIntegerField()

    objects = ReservationManager()



    def __str__(self):
        return f"{self.customer.name} - {self.restaurant.name} - {self.date} {self.time}"





