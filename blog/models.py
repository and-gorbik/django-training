from django.db import models
from django.urls import reverse

class ArticleManager(models.Manager):
    pass

class Article(models.Model):
    title = models.CharField("Title", max_length=100, default="", unique=True)
    slug = models.SlugField("Slug", max_length=120, allow_unicode=True, null=True)
    description = models.TextField("Description", default="")
    added_at = models.DateField("Added at", auto_now_add=True)
    objects = ArticleManager()

    class Meta:
        ordering = ['added_at']
    
    def get_absolute_url(self):
        return reverse('article', kwargs={'slug': self.slug})
