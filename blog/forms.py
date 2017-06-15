from django import forms

from .models import Post

#PostForm is the name of our form
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
