from django import forms
from django.forms.models import modelformset_factory

from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','description')

editPostedForm = modelformset_factory(Post,PostForm)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=('comments',)