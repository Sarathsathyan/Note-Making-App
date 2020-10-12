from django.db import models
from datetime import datetime
# Create your models here.

class Note(models.Model):
    heading = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    note = models.CharField(max_length=2000)
    created_date = models.DateField(default=datetime.now,blank=True)

    def __str__(self):
        return self.heading

