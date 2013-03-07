from django.db import models

class Fanpage(models.Model):
    name = models.CharField(max_length=200)
    url_id = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Record(models.Model):
    fanpage = models.ForeignKey(Fanpage)
    datetime = models.DateTimeField('Date and time scraped')
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s: %d" % (self.datetime, self.likes)
