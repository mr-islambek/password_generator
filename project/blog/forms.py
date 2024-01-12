from django import forms




class PasswordGeneratorForm(forms.Form):
    length = forms.IntegerField(min_value=1, max_value=32)
    include_letters = forms.BooleanField(required=False, initial=True)
    include_numbers = forms.BooleanField(required=False, initial=True)
    include_symbols = forms.BooleanField(required=False, initial=True)