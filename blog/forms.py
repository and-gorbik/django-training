from django.forms import ModelForm, ValidationError
from django.utils.text import slugify
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description']

    # the example of form validation
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if '?' in title:
            raise ValidationError("The title can't contain '?' character")
        return title
    
    def save(self, commit=True, *args, **kwargs):
        obj = super().save(commit=False, *args, **kwargs)
        # do some stuff before saving
        obj.slug = slugify(obj.title, allow_unicode=True)
        if commit:
            obj.save()
        return obj

