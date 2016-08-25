from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    telnumber = models.CharField(max_length=11,primary_key=True)
    
    class Meta:
        app_label = 'worksheet'

    def __unicode__(self):
        return u'%s' % (self.telnumber)
    

class WorkSheet(models.Model):
    sheet_number = models.CharField(max_length=200, primary_key=True)
    client_type = models.IntegerField()
    sheet_type = models.IntegerField()
    time = models.DateField()
    content = models.TextField()
    method = models.TextField()
    user = models.ForeignKey(User)
    
    class Meta:
        app_label = 'worksheet'

    def __unicode__(self):
        return u'%s' % (self.sheet_number)
    