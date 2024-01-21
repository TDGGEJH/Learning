from .models import Shodki
from django.forms import ModelForm, TextInput, Textarea

class ShodkaForm(ModelForm):
    class Meta:
        model = Shodki
        fields = ['title', 'location', 'desk']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-inp',
                'placeholder':'Имя',
            }),
            "location": TextInput(attrs={
                'class': 'form-inp',
                'placeholder':'Локация',
            }),
            "desk": Textarea(attrs={
                'class': 'form-area',
                'placeholder':'Описание',
            }),
        }