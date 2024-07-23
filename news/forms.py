from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import News, User


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'summary', 'content', 'image', 'category')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'name', 'password1', 'password2']
