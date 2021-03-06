from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class School(models.Model):
    nombre = models.CharField(max_length=256,default='')
    email = models.CharField(max_length=256,default='')
    celular = models.CharField(max_length=256,default='')
    torre = models.CharField(max_length=256,default='')
    piso = models.CharField(max_length=256,default='')
    numero_de_apartamento = models.CharField(max_length=256,default='')


    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students')

    def __str__(self):
        return self.name
