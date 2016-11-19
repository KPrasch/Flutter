from django import forms
from .models import Flutt


class FluttForm(forms.ModelForm):

    class Meta:
        model = Flutt
        fields = ('author', 'body')


class SearchForm(forms.Form):
    query_text = forms.CharField(max_length=256, required=False)
