from django import forms


class ContactForm(forms.Form):
    name= forms.CharField(max_length=500, label="Name")
    email= forms.EmailField(max_length=500, label="Email")
    comment= forms.CharField(label='',widget=forms.Textarea(
                        attrs={'placeholder': 'Enter your comment here'}))

    # def __init__(self,*args,**kwargs):
    #     super(InfoForm,self).__init__(*args,**kwargs)
    #     self.fields['contact_name'].label = "Your Name:"
    #     self.fields['contact_email'].label = "Your Email:"
    #     self.fields['content'].label = "Tell us a little bit about why you're interested in our study:"
