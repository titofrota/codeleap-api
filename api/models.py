from django.db import models


class BaseModel(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(BaseModel):
    username = models.CharField(max_length=100, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.title
