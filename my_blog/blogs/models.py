from django.db import models
from datetime import date

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    abstract = models.TextField()
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    removal_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def is_past(self):
        return date.today() >= self.removal_date.date()
