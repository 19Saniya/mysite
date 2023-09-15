from django.db import models
class Features(models.Model):
    features_icon=models.CharField(max_length=50)
    features_title=models.CharField(max_length=50)
    features_des=models.TextField()

# Create your models here.
