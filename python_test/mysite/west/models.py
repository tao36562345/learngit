from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length = 200)
    age = models.IntegerField(default = 0)
    email = models.EmailField()
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name = models.CharField(max_length = 5)
    def __unicode__(self):
        return self.name
