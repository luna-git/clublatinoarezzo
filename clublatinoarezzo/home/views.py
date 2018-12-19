from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import Testata , Titolo , Presentazione , Staff , Staffdes , Presentazionepunto , Blog , Blogdes , Footeradv , Servizi , Servizides , Contatto, Contattorichiesta

import smtplib

# Create your views here.

def  contenuto():
    context = {
        "appweb": "home",
        "testate": Testata.objects.all() ,
        "titolo": Titolo.objects.all()[0],
        "staffdes": Staffdes.objects.all()[0],
        "staffs": Staff.objects.all(),
        "presentazione": Presentazione.objects.all()[0],
        "presentazionepunti": Presentazionepunto.objects.all(),
        "blogdes": Blogdes.objects.all()[0],
        "blogs": Blog.objects.all(),
        "footeradv": Footeradv.objects.all()[0],
        "servizides": Servizides.objects.all()[0],
        "servizi": Servizi.objects.all(),
        "contatto": Contatto.objects.all()[0]
    }
    return context

def index(request):
    context = contenuto()
    context.update(numpag ="1")
    return render(request,"home/index.html", context)

def about(request):
    context = contenuto()
    context.update(numpag ="2")
    return render(request,"home/about.html", context)

def staff(request):
#    return HttpResponse("Testate")
    context = contenuto()
    context.update(numpag ="3")
    return render(request,"home/staff.html", context)

def servizi(request):
#    return HttpResponse("Testate")
    context = contenuto()
    context.update(numpag ="4")
    return render(request,"home/servizi.html", context)

def blog(request):
    context = contenuto()
    context.update(numpag ="5")
    return render(request,"home/blog.html", context)

def contact(request):
#    return HttpResponse("Testate")
    context = contenuto()
    context.update(numpag ="6")
    return render(request,"home/contact.html", context)

def galleria(request):
#    return HttpResponse("Testate")
    context = contenuto()
    context.update(numpag ="10")
    return render(request,"home/galleria.html", context)

def contactform1(request):

    nome = request.POST.get('nome', '')
    soggetto = request.POST.get('soggetto', '')
    oggetto = request.POST.get('oggetto', '')
    email = request.POST.get('email', '')
    titolo = "Da: " + email + "("+ nome +") -->" + soggetto
    to_email = Titolo.objects.all()[0].email
    crtsoggetto = "Ricevuta: " + soggetto
    crtoggetto = "La tua richiesta è stata inoltrata."
    # return HttpResponse(risposta ,"ok!!")

    if soggetto and oggetto and email and nome :
        try:
            send_mail(crtsoggetto, crtoggetto, to_email, [email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        #return HttpResponseRedirect('/index.html')

        try:
            send_mail(titolo, oggetto, email, [to_email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
                #return HttpResponseRedirect('/index.html')

        #CARICA RICHIESTA CONTTATTO SUL DB
        cr = Contattorichiesta(nome=nome , soggetto=soggetto , oggetto=oggetto, email=email)
        cr.save()
        return index(request)

    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        context = contenuto()
        context.update(numpag ="6")
#        context.update(alertmsg="Make sure all fields are entered and valid.")
        context.update(alertmsg="Assicurarsi che tutti i campi siano stati inseriti. ")
        context.update(alertclass="alert-warning")
        context.update(form1nome=nome)
        context.update(form1email=email)
        context.update(form1soggetto=soggetto)
        context.update(form1msg=oggetto)
        return render(request,"home/contact.html", context)
