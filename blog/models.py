from django.db import models
from django.utils.timezone import now

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=now, blank=True)
    document = models.TextField(max_length=10000, default="this document is blank")
    
    def __str__(self):
        return self.title
