from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField('date published')
    document = models.CharField(max_length=10000, default="this document is blank")
    
    def __str__(self):
        return self.title
