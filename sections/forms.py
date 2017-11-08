from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255, 
            widgets=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label='Email', max_length=255, 
            widgets=forms.TextInput(attrs={'placeholder': 'Email'}))
    request = forms.CharField(label='Request', max_length=255, 
            widgets=forms.TextInput(attrs={'placeholder': 'Request'}))
