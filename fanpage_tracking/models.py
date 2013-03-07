from django.db import models

class Fanpage(models.Model):
    name = models.CharField(max_length=200)
    url_id = models.CharField(max_length=200)
    creation_date = models.DateTimeField('Date and time tracking began')

    def __unicode__(self):
        return self.name

class DayLikes(models.Model):
    fanpage = models.ForeignKey(Fanpage)
    datetime = models.DateTimeField('Date and time scraped')
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s: %d" % (self.datetime, self.likes)
