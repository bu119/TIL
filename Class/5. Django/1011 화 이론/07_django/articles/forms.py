from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        # fields = ('title', 'content', 'image',)
        # exclude = ('title',)
        exclude = ('user',)  # 외래키 제외


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('article', 'user',)