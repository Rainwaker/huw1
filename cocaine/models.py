
from django.db import models
from django.utils import timezone

class Experience(models.Model):
    name = models.ForeignKey('auth.User')
    type = models.CharField(max_length=10)
    Start_Date = models.DateTimeField(
             blank=True, null=True)
    End_Date = models.DateTimeField(
             blank=True, null=True)
    Published_Date = models.DateTimeField(
             default=timezone.now)
    title = models.CharField(max_length=120)
    description = models.TextField()

    def publish(self):
        self.Published_Date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
