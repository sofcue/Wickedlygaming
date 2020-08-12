from django import forms
from .models import Post, Videos, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'status', 'image')


class VideoForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ('name', 'video')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)
