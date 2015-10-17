from django.db import models


class Entry(models.Model):
    sitzung = models.CharField(max_length = 255)
    tpunkt = models.CharField(max_length = 255)
    text = models.TextField()
    datum = models.DateTimeField()
    upvotes = models.IntegerField(default = 0)
    downvotes = models.IntegerField(default = 0)
