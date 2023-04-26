from django import forms
from .models import Blog


class BlogFrom(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'published_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'update_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}),
            'content': forms.Textarea(attrs={'class':'form-control'})
        }