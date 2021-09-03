from django.db import models

# Create your models here.




class Adhar_no(models.Model):

    aadhar_no=models.IntegerField()


    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name





class Center(models.Model):
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


