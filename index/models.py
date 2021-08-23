from typing import ChainMap
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=36, blank=True)
    description = models.TextField(max_length=256, blank=False)

    def __str__(self):
        return self.title
