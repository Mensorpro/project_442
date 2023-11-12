from django import forms
from .models import  ConverstionMessage

class ConverstionMessageForm(forms.ModelForm):
    class Meta:
        model = ConverstionMessage
        fields = ['text',]
        labels = {'text': 'Message',}
        widgets = {'text': forms.Textarea(attrs={
            'cols': 80,
            'rows': 5,
            'placeholder': 'Type your message here',
            'class': 'form-control w-full px-3 py-2 text-base leading-tight text-gray-700 border rounded-xl shadow appearance-none focus:outline-none focus:shadow-outline',
            'style': 'resize:none;'}),
        }

