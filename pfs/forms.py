from django import forms

class CountryForm(forms.Form):
    search_term = forms.CharField(label='Search for country', max_length=30)

