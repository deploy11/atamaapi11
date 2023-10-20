from django.db import models

# Create your models here.
class Atama(models.Model):
    nomi = models.CharField(max_length=500)
    type = models.CharField(max_length=500)
    uzb = models.CharField(max_length=500)
    eng = models.CharField(max_length=500)
    rus = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.nomi