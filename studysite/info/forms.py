from django import forms
from .models import ContactMod

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMod
        fields = {'name','email','comment'}
        field_order = ['name','email','comment',]

        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Your Name','style': 'width:270px;margin-bottom:.5rem;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Your Email','style': 'width:270px; margin-bottom:.5rem;'}),
            'comment': forms.Textarea(attrs={'class': 'form-control','placeholder':"Tell us about yourself, and why you're interested in the study!"}),
        }
