from django import forms
from .models import *

class BookingForm(forms.ModelForm):
    class Meta:
        model= Booking
        fields='__all__'
        widgets={'Date':forms.DateInput()}

    def __init__(self,*args,**kwargs):
        super().__init__(*args ,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'
            field.widget.attrs['placeholder']='YOUR  '+field.label
            field.widget.attrs['style']='width:400px; height:40px;'
           
