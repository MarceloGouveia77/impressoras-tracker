from django import forms
from crawler.models import Impressora

class ImpressoraForm(forms.ModelForm):

    class Meta:
        model = Impressora

        fields = '__all__'