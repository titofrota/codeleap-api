from django.db import models
from .basemodel import BaseModel

class Post(BaseModel):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
    