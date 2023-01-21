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
class Guestpostform(forms.ModelForm):
    class Meta:
        model = Guestpost
        fields='__all__'
        widgets = {'excerpt':forms.Textarea(attrs={'rows':'2','height':'none'})}
        labels={
            'Author':'Your Name',
            'email':'Your Email',
            'title':'Blog Title',
            'excerpt':'Snippet',
            'content':'Content'
        }

