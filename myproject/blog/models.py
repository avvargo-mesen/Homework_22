from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        ordering = ['title']
