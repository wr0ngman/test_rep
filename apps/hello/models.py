from django.db import models

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
