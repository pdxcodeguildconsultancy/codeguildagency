from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, Context
from django.shortcuts import render_to_response
from django.core.mail import send_mail, BadHeaderError
from pdxcodeguild.forms import PostForm, Contact
# Create your views here.


def index(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('index.html', context_dict, context)


def about(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('about.html', context_dict, context)


def advisors(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('advisors.html', context_dict, context)


def apply(request):
    context = RequestContext(request)
    if request.method == 'GET':
        form = Contact()
    else:
        # A POST request: Handle Form Upload
        form = Contact(request.POST)  # Bind data from request.POST into a PostForm

        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            phone_number = form.cleaned_data['phone_number']
            email_address = form.cleaned_data['email_address']
            best_contact = form.cleaned_data['best_contact']
            message = form.cleaned_data['message']

            from django.core.mail import EmailMultiAlternatives

            subject, from_email, to = '%s filled out the Interested form'% full_name, 'forms@pdxcodeguild.com', 'sheri.dover@gmail.com'
            text_content = '''Name: %s
            Phone number: %s
            Email address: %s
            How do you prefer to be contacted? %s
            Message: \n %s'''% (full_name, phone_number, email_address, best_contact, message)
            html_content = 'Full name: %s<br>Phone number: %s<br>Email address: %s<br>How do you prefer to be contacted? %s<br>Message:<br> %s'% (full_name, phone_number, email_address, best_contact, message)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponseRedirect('/thanks/')
    context_dict = {'form': form}

    return render_to_response('apply.html', context_dict, context)


def contact(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('contact.html', context_dict, context)


def faq(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('faq.html', context_dict, context)


def gettechnical(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('gettechnical.html', context_dict, context)


def individualized(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('individualized.html', context_dict, context)


def jrdevbootcamp(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('jrdevbootcamp.html', context_dict, context)


def evening_bootcamp(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('evening-bootcamp.html', context_dict, context)


def partner(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('partner.html', context_dict, context)


def program(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('program.html', context_dict, context)


def sponsor(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('sponsor.html', context_dict, context)


def team(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('team.html', context_dict, context)


def thanks(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('thanks.html', context_dict, context)


def value(request):
    context = RequestContext(request)
    context_dict = {}

    return render_to_response('value.html', context_dict, context)


