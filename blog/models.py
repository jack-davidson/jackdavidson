from django.db import models
from django.utils.timezone import now
import re

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=now, blank=True)
    document = models.TextField(max_length=10000, default="this document is blank")

    # preview document. Returns first 50 characters with html tags removed.
    def preview(self):
        return re.compile(r'<[^>]+>').sub('', self.document[:50])
    
    def __str__(self):
        return self.title
