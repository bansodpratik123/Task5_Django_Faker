from django.db import models

# Create your models here.
class Fake_Students(models.Model):
    Name=models.CharField(max_length=50)
    Percentage=models.FloatField()
    Email=models.EmailField()
    City=models.CharField(max_length=50)
    MobNo=models.IntegerField(blank=True, null=True)