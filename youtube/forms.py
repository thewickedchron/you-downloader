from django import forms

class SingleForm(forms.Form): 
    single_link = forms.CharField(max_length=250, label="Enter Link")
