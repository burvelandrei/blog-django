from django.db import models
from django.utils import timezone


class TimeStappedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Publication(TimeStappedModel):
    title = models.CharField(max_length=255, null=False)
    content = models.TextField()

    def __str__(self):
        return self.title
