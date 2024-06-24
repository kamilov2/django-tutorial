from django import forms 
from . models import Leaguage,Club,Player

class AddLeaguageForm(forms.ModelForm):
    
    
    class Meta:
        model = Leaguage
        fields = ["name","logo","country"]
        widtgets = {}
        labels = {}

