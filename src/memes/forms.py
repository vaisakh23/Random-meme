from django import forms

class SaveMemeForm(forms.Form):
    img_url = forms.CharField(max_length=140, widget=forms.HiddenInput())

#class RemoveMemeForm(forms.Form):
    
