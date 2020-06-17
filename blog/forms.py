from django import forms
from .models import Post, Videos


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'status')

class VideoForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ('name', 'video')