from django.db import models


class Peak(models.Model):
    peak_name = models.CharField(max_length=200)
    peak_coordinates = models.IntegerField(default=0)
    peak_height = models.IntegerField(default=0)
    user_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)
    peak_image = models.ImageField(null=True)


    def __str__(self):
        return self.peak_name


