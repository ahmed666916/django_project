from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
        ordering = ['-published_at']
