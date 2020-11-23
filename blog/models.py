from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.title
