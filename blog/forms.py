from django import forms

from .models import Post
from .models import Comment



#PostForm is the name of our form
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

#Comments
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
