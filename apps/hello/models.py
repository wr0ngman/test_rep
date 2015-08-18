from django.db import models

# Create your models here.
class ident(models.Model):

    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    birthdate = models.DateField()
    bio = models.TextField()    
    email = models.EmailField()
    jabber = models.CharField(max_length=100)
    skype = models.CharField(max_length=100)
    othcontacts = models.TextField()
    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s'%(self.name, self.lastname, self.birthdate, self.bio, self.email, self.jabber, self.skype, self.othcontacts)
