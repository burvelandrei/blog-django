from django.db import models
from publication.models import Publication
from django.utils import timezone


class TimeStappedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Comment(TimeStappedModel):
    publication = models.ForeignKey(
        Publication, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField()

    def __str__(self):
        return f"Comment on {self.publication.title}"
