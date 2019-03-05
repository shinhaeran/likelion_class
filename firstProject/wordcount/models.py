from django.db import models

class Words(models.Model):
    text = models.CharField(max_length=100,primary_key=True)
    frequency_total = models.IntegerField(default = 0)
# Create your models here.
