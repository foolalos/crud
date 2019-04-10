# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Empleados(models.Model):
	nombre = models.CharField(max_length = 60)
	puesto = models.CharField(max_length = 60)
	numempleado = models.IntegerField(blank=False)
	email= models.EmailField()
	def __str__(self):
    	    return self.nombre