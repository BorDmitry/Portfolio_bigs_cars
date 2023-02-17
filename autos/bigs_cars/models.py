from django.db import models


class BigsCars(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='bigs_cars/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title