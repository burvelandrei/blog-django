from django import forms
from .models import Publication

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'content']
        labels = {
            'title': 'Название публикации',
            'content': 'Текст публикации',
        }