from django.db import models

# Create your models here.
class countries(models.Model):
    ID = models.CharField(max_length=50,primary_key=True)
    CountryCode= models.CharField(max_length=30)
    Country = models.CharField(max_length=30)
    NewConfirmed = models.IntegerField(default=0)
    TotalConfirmed = models.IntegerField(default=0)
    NewDeaths = models.IntegerField(default=0)
    TotalDeaths = models.IntegerField(default=0)
    NewRecovered = models.IntegerField(default=0)
    TotalRecovered = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    