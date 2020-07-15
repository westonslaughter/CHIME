from django.shortcuts import render
from django.views.generic import View, TemplateView
# 'Contact Us' Form
from info.forms import InfoForm
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

# class InfoView(TemplateView):
    # template_name='info.html'

def Info(request):
    form_class = InfoForm

    # logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            # email = EmailMessage(
            #     "New contact form submission",
            #     content,
            #     "California Health Impacts from Mining Exposure" +'',
            #     ['westonslaughter@gmail.com'],
            #     headers = {'Reply-To': contact_email }
            # )

            email = send_mail('CHIME Participant',
             contact_name,
             'wslaughter@berkeley.edu',
             [contact_email],
             fail_silently=False)

            # email.send()
            return redirect('info')

    return render(request, 'info.html', {
        'form': form_class,
    })
