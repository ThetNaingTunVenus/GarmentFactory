from django import forms
from .models import *
from django.contrib.auth.models import User

class EditOrderQtyForm(forms.ModelForm):
    class Meta:
        model = OrderQty
        fields =['style','making_charge','import_export_charge','box_charge','poly_bag','sewing_thread']
        widgets = {
            'style': forms.TextInput(attrs={'class': 'form-control col-md-6','readonly':'True'}),
            'making_charge': forms.NumberInput(attrs={'class': 'form-control'}),
            'import_export_charge': forms.NumberInput(attrs={'class': 'form-control'}),
            'box_charge': forms.NumberInput(attrs={'class': 'form-control'}),
            'poly_bag': forms.NumberInput(attrs={'class': 'form-control'}),
            'sewing_thread': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class OrderDeliveryForm(forms.ModelForm):
    class Meta:
        model = OrderQty
        fields = ['delivery']

class OrderETAForm(forms.ModelForm):
    class Meta:
        model = OrderQty
        fields = ['id','fabricETA','accETA']



class ProductionLineForm(forms.ModelForm):
    class Meta:
        model = ProductionLine
        fields = '__all__'
        widgets = {
            'ProductionLine': forms.NumberInput(attrs={'class': 'form-control'}),
        }
