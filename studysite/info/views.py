from django.shortcuts import render
from django.views.generic import View, TemplateView
# 'Contact Us' Form
# from info.forms import InfoForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.core.mail import send_mail


# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'

class StudyView(TemplateView):
    template_name='study.html'

class UsView(TemplateView):
    template_name='us.html'

class ThanksView(TemplateView):
    template_name='thanks.html'

# class InfoView(TemplateView):
    # template_name='info.html'

from .forms import ContactForm


def contactview(request):
    name=''
    email=''
    comment=''


    form= ContactForm(request.POST or None)
    if form.is_valid():
        name= form.cleaned_data.get("name")
        email= form.cleaned_data.get("email")
        comment=form.cleaned_data.get("comment")


        subject= "A Visitor's Comment"


        comment= name + " with the email, " + email + ", sent the following message:\n\n" + comment;
        send_mail(subject, comment, 'chimecontact@gmail.com', ['chimecontact@gmail.com'])


        context= {'form': form}

        return render(request, 'thanks.html', context)

    else:
        context= {'form': form}
        # Maybe should make, an "oops!" form?
        return render(request, 'info/info.html', context)
