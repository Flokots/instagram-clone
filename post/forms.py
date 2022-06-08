from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    image = forms.ImageField(required=True)
    caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Caption'}), required=True)
    tag = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Tags - Seperate tags with comma'}), required=True)

    class Meta:
        model = Post
        fields = ['name', 'image', 'caption', 'tag']
