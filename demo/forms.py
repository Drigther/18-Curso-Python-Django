from django import forms
from demo.models import *

class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elemento