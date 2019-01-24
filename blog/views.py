from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleForm

def articles(request, *args, **kwargs):
    objs = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': objs})

def article(request, *args, **kwargs):
    obj = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article.html', {'article': obj})

def create_article(request, *args, **kwargs):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)

    return render(request, 'blog/form.html', {'article_form': form})

