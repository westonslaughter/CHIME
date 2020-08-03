from django.shortcuts import render
from django.views.generic import View, TemplateView, DetailView, ListView
# 'Contact Us' Form
from . import models
# from info.forms import InfoForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.core.mail import send_mail


# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'

class UsView(TemplateView):
    template_name='us.html'

class ThanksView(TemplateView):
    template_name='thanks.html'

class StudyView(ListView):
    template_name='study.html'
    model = models.Study
    context_object_name = 'Studies'


# class InfoView(TemplateView):
    # template_name='info.html'

from .forms import ContactForm


def contactview(request):
    name=''
    email=''
    comment=''


    form = ContactForm(request.POST or None)
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
        return render(request, 'info.html', context)

# Staff Page
class OrgListView(ListView):
    context_object_name = 'Orgs'
    model = models.Org
    template_name = 'info/org_list.html'

class StaffDetailView(DetailView):
    context_object_name = 'staff_detail'
    model = models.Org
    template_name = 'info/staff_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StaffDetailView, self).get_context_data(**kwargs)
        page_one = models.Org.objects.get(id=self.kwargs.get('pk', ''))
        context['page_one'] = page_one
        return context

class StaffContactView(DetailView):
    context_object_name = 'staff_contact'
    model = models.Org
    template_name = 'info/staff_contact.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super(StaffContactView, self).get_context_data(**kwargs)
        page_alt = models.Org.objects.get(id=self.kwargs.get('pk','')).employees.get(id=self.kwargs.get('pk_alt', ''))
        context['page_alt'] = page_alt
        # context['form'] = ContactForm
        return context

# ONE DAY: Individual contact forms. Time/Effort vs Reward has been
# WAY off on this project. Abandoning for now.

    # def emailme(self,request,*args,**kwargs):
    #     name=''
    #     email=''
    #     comment=''
    #
    #     form = self.form_class(request.POST)
    #
    #     if form.is_valid():
    #         name= form.cleaned_data.get("name")
    #         email= form.cleaned_data.get("email")
    #         comment= form.cleaned_data.get("comment")
    #
    #
    #         subject= "A Visitor's Comment"
    #
    #
    #         comment= name + " with the email, " + email + ", sent the following message:\n\n" + comment;
    #
    #         send_mail(subject, comment, 'chimecontact@gmail.com', ['chimecontact@gmail.com'])
    #
    #
    #         context= {'form': form}
    #
    #         return render(request, 'thanks.html', context)
    #
    #     else:
    #         context= {'form': form}
    #         # Maybe should make, an "oops!" form?
    #         return render(request, 'staff_contact.html', context)
