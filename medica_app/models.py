from __future__ import unicode_literals

from django.db import models

GENDER = (
    ("Hombre","Hombre"),
    ("Mujer","Mujer"),
)



class Paciente(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, blank=True, default='')
	last_name = models.CharField(max_length=50, blank=True, default='')
	gender = models.CharField(max_length=10,choices=GENDER)
	age = models.IntegerField(null=True)
	phone = models.CharField(max_length=20, blank=True, default='')
	adress = models.CharField(max_length=150, blank=True, default='')
	postal_code = models.IntegerField(null=True)
	email = models.EmailField(max_length=100, blank=True, default='')
	password = models.CharField(max_length=20, blank=True, default='')
	
	
	class Meta:
		ordering = ('name',)

	def __str__(self):
			return "Paciente: %s %s" % (self.name,self.last_name)

class Medico(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, blank=True, default='')
	last_name = models.CharField(max_length=50, blank=True, default='')
	gender = models.CharField(max_length=10,choices=GENDER)
	age = models.IntegerField(null=True)
	professional_id = models.CharField(max_length=150, blank=True, default='')
	phone = models.CharField(max_length=20, blank=True, default='')
	email = models.EmailField(max_length=100, blank=True, default='')
	password = models.CharField(max_length=20, blank=True, default='')
	

	class Meta:
		ordering = ('name',)

	def __str__(self):
			return "Medico: %s %s" % (self.name,self.last_name)

class Cita(models.Model):
	id = models.AutoField(primary_key=True)
	paciente = models.ForeignKey(Paciente)
	medico = models.ForeignKey(Medico)
	date = models.CharField(max_length=50, blank=True, default='')

	class Meta:
		ordering = ('id',)

	def __str__(self):
			return "Cita: %s | %s | %s | %s" % (self.id,self.paciente,self.medico,self.date)

	

class Consultorio(models.Model):
	id = models.AutoField(primary_key=True)
	medico = models.ForeignKey(Medico)
	adress = models.CharField(max_length=150, blank=True, default='')
	postal_code = models.IntegerField(null=True)

	class Meta:
		ordering = ('id',)

class Historial(models.Model):
	id = models.AutoField(primary_key=True)
	cita = models.ForeignKey(Cita)
	observaciones = models.CharField(max_length=250, blank=True, default='')

	







