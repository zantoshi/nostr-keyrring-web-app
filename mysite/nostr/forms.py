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

class BadgeDefinitionForm(forms.Form):
    unique_name = forms.CharField(max_length=500)
    name = forms.CharField(max_length=500)
    description = forms.CharField(max_length=500)
    image = forms.URLField()
    thumb = forms.URLField()

class BadgeAwardForm(ModelForm):
    class Meta:
        model = BadgeAward
        fields = ['badge_definition', 'awardee_pubkey']