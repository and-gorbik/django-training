from django.forms import ModelForm, ValidationError
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