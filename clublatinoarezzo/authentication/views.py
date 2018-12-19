from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from home.models import Testata , Titolo , Presentazione , Staff , Staffdes , Presentazionepunto , Blog , Blogdes , Footeradv , Servizi , Servizides , Contatto, Contattorichiesta
from blog.models import Testatablog , Articoloblog , Categoriablog

# Create your views here.
def  contenuto():
    context = {
        "appweb": "Login Cla",
        "testate": Testata.objects.all() ,
        "titolo": Titolo.objects.all()[0],
        "staffdes": Staffdes.objects.all()[0],
        "presentazione": Presentazione.objects.all()[0],
        "presentazionepunti": Presentazionepunto.objects.all(),
        "blogdes": Blogdes.objects.all()[0],
        "blogs": Blog.objects.all(),
        "footeradv": Footeradv.objects.all()[0],
        "servizides": Servizides.objects.all()[0],
        "contatto": Contatto.objects.all()[0],
        "testatablog": Testatablog.objects.all()[0],
        "articoliblog": Articoloblog.objects.all(),
        "categorieblog": Categoriablog.objects.all()
    }
    return context

def index(request):
    context = contenuto()
    context.update(numpag ="1")

    # crt presenza del urldiritorno
    if 'urldiritorno' in request.session :
        #get urldiritorno
        urldiritorno = request.session['urldiritorno']
    else:
        # costruzione del urldiritorno
        lpath=request.path.split('/')
        urldiritorno=lpath[1]+"index"
        # set urldiritorno
        request.session['urldiritorno'] = urldiritorno
        #urldiritorno_save = request.session['urldiritorno']

    if not request.user.is_authenticated:
        return render(request, "authentication/login.html", context,{"message": None})
    # context user
    context.update(user=request.user)
#    lpath=request.path.split('/')
#    appweb=lpath[1]
#    lpath[-1]=".html"
#    lpath[1:1]="authentication/"
#    urldiritorno=''.join(lpath)
#    context.update( appweb = appweb )
#    return render(request, urldiritorno , context)

#    lpath=request.path.split('/')
#    urldiritorno=lpath[1]+"index1"

    return HttpResponseRedirect(reverse(urldiritorno))

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "authentication/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "authentication/login.html", {"message": "Logged out."})
