from django import forms
from django.forms import ModelForm
from .models import Data_set

class DateFrom(forms.Form):
    from_date=forms.DateField(label="From ") 
    to_date=forms.DateField(label="To ")

    #class Meta:
     #   model = Data_set
      #  fields = ('created_date','created_date',)
