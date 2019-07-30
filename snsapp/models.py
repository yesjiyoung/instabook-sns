from django.db import models
from django.utils.timezone import now

class Sns(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateTimeField('date published')
    body = models.TextField()
    img = models.TextField(default="")

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]
    

