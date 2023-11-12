from django import forms
from .models import Item, Category

INPUT_CLASS = 'form-control form-control-sm w-full px-3 py-2 text-base leading-8 text-gray-700 bg-white border border-gray-300 rounded-xl outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'category', 'image')

        widgets = {
            'category': forms.Select(attrs={'class': INPUT_CLASS}),
            'name': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASS}),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASS}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASS}),

        } 
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price','is_sold', 'image')

        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASS}),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASS}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASS}),

        } 
        
    