from django import forms
from django.forms.models import modelformset_factory

from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','description')

editPostedForm = modelformset_factory(Post,PostForm)