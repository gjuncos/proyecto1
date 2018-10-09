from django.db import models

# Create your models here.

class Contacto(models.Model):
	#django pone un campo id autoincrementable en la base de datos
	telefono = models.CharField(max_length=20)
