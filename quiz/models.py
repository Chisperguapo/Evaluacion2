from django.db import models

class Dato(models.Model):
    nombre=models.CharField(max_length=50)
    ficha=models.IntegerField()
    edad=models.IntegerField()
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'dato'
        verbose_name_plural = 'datos'

    def __str__(self):
        return self.nombre

