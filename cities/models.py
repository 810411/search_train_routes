from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=128, verbose_name='Город')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']

    def __str__(self):
        return self.name
