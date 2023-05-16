from django.db import models

# Create your models here.
class Movie(models.Model):
    hall = models.CharField(max_length=10)
    Movie = models.CharField(max_length=10)
    
    date = models.DateField()
    def __str__(self):
        return self.Movie
    
    

class Guest(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.IntegerField()
    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    Guest = models.ForeignKey(Guest,related_name='reservations' ,on_delete= models.CASCADE)
    Movie = models.ForeignKey(Movie,related_name="reservations" , on_delete =models.CASCADE)
    
    

