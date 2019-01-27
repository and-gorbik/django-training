from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Article
from .forms import ArticleForm

def paginate(lst, page=1, count=10):
    p = Paginator(lst, count)
    try:
        objects = p.page(page)
    except PageNotAnInteger:
        objects = p.page(1)
    except EmptyPage:
        objects = p.page(p.num_pages)

    return objects

# class-based views

class ArticleDetail(DetailView):
    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'article'

class ArticleList(ListView):

    def get(self, request):
        page = request.GET.get('page')
        articles = paginate(Article.objects.all(), page, count=3)
        return render(request, 'blog/index.html', {'articles': articles})

class ArticleCreate(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/add.html'

    def get_success_url(self):
        return reverse('article',args=(self.object.slug,))

class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/update.html'

    def get_success_url(self):
        return reverse('article',args=(self.object.slug,))

class ArticleDelete(DeleteView):
    model = Article
    template_name = 'blog/confirm.html'
    success_url = reverse_lazy('articles')

# # function-based views

# def articles(request, *args, **kwargs):
#     page = request.GET.get('page')
#     objs = paginate(Article.objects.all(), page, count=3)
#     return render(request, 'blog/index.html', {'articles': objs})

# def article(request, slug, *args, **kwargs):
#     article = get_object_or_404(Article, slug=slug)
#     return render(request, 'blog/article.html', {'article': article})

# def create_article(request, *args, **kwargs):
#     form = ArticleForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             obj = form.save()
#             return redirect(obj)

#     return render(request, 'blog/add.html', {'form': form})

# def update_article(request, slug, *args, **qwargs):
#     article = get_object_or_404(Article, slug=slug)
#     form = ArticleForm(request.POST or None, instance=article)
#     if request.method == 'POST':
#         if form.is_valid():
#             obj = form.save()
#             return redirect(obj)
#     return render(request, 'blog/update.html', {'form': form})

# def delete_article(request, slug, *args, **kwargs):
#     article = get_object_or_404(Article, slug=slug)
#     if request.method == 'POST':
#         article.delete()
#         return redirect('articles')
#     return render(request, 'blog/confirm.html', {'article': article})