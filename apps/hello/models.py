from django.db import models

# Create your models here.
class info(models.Model)
	name = models.CharField(max_length='250')
	def __str__(self):
		return u'$ $'%('Info about:',self.name)
