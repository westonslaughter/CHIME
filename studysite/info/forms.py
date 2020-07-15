from django import forms

# Info/COntact forms
class InfoForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self,*args,**kwargs):
        super(InfoForm,self).__init__(*args,**kwargs)
        self.fields['contact_name'].label = "Your Name:"
        self.fields['contact_email'].label = "Your Email:"
        self.fields['content'].label = "Tell us a little bit about why you're interested in our study:"
