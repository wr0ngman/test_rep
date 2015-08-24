from django.db import models

<<<<<<< HEAD
""" Subscribe developer information model fields """
class Devinfo(models.Model):

    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    birthdate = models.DateField()
    bio = models.TextField()    
    email = models.EmailField()
    jabber = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)
    othcontacts = models.TextField()
    def __unicode__(self):
        return u'Information about: %s %s email:%s ;jabber:%s'%(self.name, self.lastname, self.email, self.jabber)
=======
# Create your models here.
<<<<<<< HEAD
class info(models.Model)
	name = models.CharField(max_length='250')
	def __str__(self):
		return u'$ $'%('Info about:',self.name)
>>>>>>> fa3a7ceb5e6502def0a5cf344dacc4caf328e0bf
=======
>>>>>>> 16471ac88aab49acf3f2ee3c57acb89ee00ae1ba
