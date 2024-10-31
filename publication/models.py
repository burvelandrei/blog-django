from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=255, null=False)
    content = models.TextField()

    def __str__(self):
        return self.title
