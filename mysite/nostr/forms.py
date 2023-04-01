from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from markdownx.fields import MarkdownxFormField
from .models import *

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['title']


class BlogForm(forms.Form):
    content = MarkdownxFormField()