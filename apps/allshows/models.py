from __future__ import unicode_literals
from django.db import models


class Tvshowmanager(models.Manager):
    def basic_validator(self,postData):
        errors ={}
        if len(postData['title']) <2:
            errors['title'] = "why you lyin?!"
        if len(postData['network']) <2:
            errors['network'] = "Damn Gina!!!"
        if not (postData['date']):
            errors['date'] = 'Great Scott!!'
        if len(postData['desc']) <10:
            errors['desc'] = 'Listen Linda!'
        return errors

class Tvshow(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    date = models.DateField()
    desc = models.CharField(max_length=255)
    objects = Tvshowmanager()
