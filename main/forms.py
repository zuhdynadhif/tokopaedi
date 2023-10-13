from django.forms import ModelForm
from . import models

from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'price', 'description', 'amount']
        # tugas 5: tambahkan class form-control untuk bootstrap
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
            'amount' : forms.NumberInput(attrs={'class':'form-control'}),
        }