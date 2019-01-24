from django.db import models

class ArticleManager(models.Manager):
    pass

class Article(models.Model):
    title = models.CharField("Title", max_length=100, default="")
    description = models.TextField("Description", default="")
    added_at = models.DateField("Added at", auto_now_add=True)
    objects = ArticleManager()

    class Meta:
        ordering = ['added_at']
