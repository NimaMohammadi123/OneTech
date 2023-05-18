from django import forms
from .models import CommentPost

class CommentForm(forms.Form):
    email = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(max_length=200 , widget=forms.TextInput(attrs={'class':'form-control'}))
