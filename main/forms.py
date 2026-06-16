from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'description',
            'color',
            'category',
        ]
        widgets = {
            'name': forms.TextInput( attrs={
                'placeholder': "Ведите имя", 
                'class': 'inpur_class'
            }),
            'price': forms.TextInput( attrs={
                'placeholder': "Ведите цену", 
                'class': 'inpur_class'
            }),
            'description': forms.NumberInput( attrs={
                'placeholder': "Ведите описание", 
                'class': 'inpur_class'
            }),
            'color': forms.TextInput( attrs={
                'placeholder': "Ведите цвет", 
                'class': 'inpur_class'
            }),
            'category': forms.TextInput( attrs={
                'placeholder': "Ведите категорийю", 
                'class': 'inpur_class'
            })

        }