from dataclasses import fields
from logging import exception
from django import forms
from blog.models import BlogPost


class BlogModelForm(forms.ModelForm):
    
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'author']
        


class BlogUpdateForm(forms.ModelForm):
    
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'update_date']

class BlogDeleteForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title']