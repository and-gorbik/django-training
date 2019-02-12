from django import forms
from django.contrib.auth import get_user_model, authenticate
from .models import Profile

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'placeholder': 'login', 'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # user = authenticate(username=username, password=password)
        # if not user:
        #     raise forms.ValidationError("Invalid credentials")
        user = get_user_model().objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError("Invalid credentials")
        if not user.check_password(password):
            raise forms.ValidationError("Invalid credentials")
        return super().clean(*args, **kwargs)


class UserCreationForm(forms.ModelForm):
    avatar = forms.ImageField(
        label='Your photo',
        required=False,
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
    )

    class Meta:
        model = get_user_model()
        fields = ('username',)
    
    def clean_password2(self):
        p1 = self.cleaned_data.get('password1')
        p2 = self.cleaned_data.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Passwords don\'t match')
        return p2

    def clean_avatar(self):
        img = self.cleaned_data.get('avatar')
        return img

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
            Profile.objects.create(user=user, avatar=self.cleaned_data.get('avatar'))
        return user