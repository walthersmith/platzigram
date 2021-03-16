""" POst forms."""

#django 
from django import forms
from django.db.models import fields
 #models
from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    """ Post model form. """ 
    
    class Meta:
        """Form Settings"""
        model = Post
        fields = ('user','profile','title','photo')


    
class CommentForm(forms.ModelForm):
    """comments models form"""

    class Meta:
        """Form settings"""
        model = Comment
        fields =('comment',)