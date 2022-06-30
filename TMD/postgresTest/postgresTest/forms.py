from django import forms
from django.forms import fields
from postgresTest.models import InventoryModel

class InventoryForms(forms.ModelForm):
    class Meta:
        model=InventoryModel
        fields="__all__"