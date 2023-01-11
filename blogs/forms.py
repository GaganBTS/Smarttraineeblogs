from django import forms
from .models import *
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ['post']
        widgets = {'comment':forms.Textarea(attrs={'oninput':'countWord()'})}
        labels ={
            'user_name':'Your Name',
            'email':'Your Email',
            'comment':'Your Comment'

        }

