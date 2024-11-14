from django.db import models
from users.models import CustomUser


class TimeStappedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Publication(TimeStappedModel):
    title = models.CharField(max_length=255, null=False)
    content = models.TextField()
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="publications"
    )

    def __str__(self):
        return self.title
