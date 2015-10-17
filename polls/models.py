from django.db import models


class Entry(models.Model):
    sitzung = models.CharField(max_length = 255)
    tpunkt = models.CharField(max_length = 255)
    text = models.TextField()
    datum = models.DateTimeField()
    upvotes = models.IntegerField(default = 0)
    downvotes = models.IntegerField(default = 0)
    total = models.IntegerField(default = 0)

    def __str__(self):
        return self.tpunkt

    def upvotepercent(self):
        self.total = self.upvotes + self.downvotes
        if (self.upvotes + self.downvotes)==0:
            return 0
        else:
            return round(self.upvotes / (self.upvotes + self.downvotes) * 100)

    def downvotepercent(self):
        self.total = self.upvotes + self.downvotes
        if (self.upvotes + self.downvotes)==0:
            return 0
        else:
            return 100 - round(self.upvotes / (self.upvotes + self.downvotes) * 100)
