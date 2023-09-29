from django import forms
from .models import Post

# class SendPostForm(forms.Form):
#     recipient = forms.CharField(max_length=100, label='Электронная почта')
#     message = forms.CharField(widget=forms.Textarea, label='Текст сообщения')

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)