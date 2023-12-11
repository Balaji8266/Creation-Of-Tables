from django.db import models

# Create your models here.

class country(models.Model):
    c_id = models.IntegerField(primary_key=True)
    C_name = models.CharField(max_length=100)

    def __str__(self):
        return self.C_name

class capital(models.Model):
    c_id=models.OneToOneField(country,on_delete=models.CASCADE)
    cap_name=models.CharField(max_length=100)

    def __str__(self):
        return self.cap_name


