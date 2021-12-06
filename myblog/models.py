from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True, db_index=True)
    title = models.TextField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
