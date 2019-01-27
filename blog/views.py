from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm
from django.forms import ValidationError
from django.utils.text import slugify

def articles(request, *args, **kwargs):
    objs = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': objs})

def article(request, slug, *args, **kwargs):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/article.html', {'article': article})

def create_article(request, *args, **kwargs):
    form = ArticleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save()
            return redirect(obj)

    return render(request, 'blog/add.html', {'form': form})

def update_article(request, slug, *args, **qwargs):
    article = get_object_or_404(Article, slug=slug)
    form = ArticleForm(request.POST or None, instance=article)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save()
            return redirect(obj)
    return render(request, 'blog/update.html', {'form': form})

def delete_article(request, slug, *args, **kwargs):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        article.delete()
        return redirect('articles')
    return render(request, 'blog/confirm.html', {'article': article})