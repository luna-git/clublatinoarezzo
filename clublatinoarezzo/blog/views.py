from django.shortcuts import render
from home.models import Testata , Titolo , Presentazione , Staff , Staffdes , Presentazionepunto , Blog , Blogdes , Footeradv , Servizi , Servizides , Contatto, Contattorichiesta
from blog.models import Testatablog , Articoloblog , Categoriablog

# Create your views here.
def  contenuto(request):
    context = {
        "appweb": "blog",
        "titolo": Titolo.objects.all()[0],
        "staffdes": Staffdes.objects.all()[0],
        "presentazione": Presentazione.objects.all()[0],
        "blogdes": Blogdes.objects.all()[0],
        "footeradv": Footeradv.objects.all()[0],
        "servizides": Servizides.objects.all()[0],
        "contatto": Contatto.objects.all()[0],
        "testatablog": Testatablog.objects.all()[0],
        "articoliblog": Articoloblog.objects.all(),
        "categorieblog": Categoriablog.objects.all(),
        "user" : request.user
    }
    return context

def clablog(request):
    context = contenuto(request)
    context.update(numpag ="1")
    return render(request,"blog/index.html", context)

def clablog_id(request, art_id):
    try:
        articolo = Articoloblog.objects.get(pk=art_id)
    except Articoloblog.DoesNotExist:
        raise Http404("Il blog ricercato non esiste.")
    context = contenuto(request)
    context.update(numpag ="2")
    context.update(art_id=art_id)
    return render(request,"blog/index.html", context)

def clablog_cat(request, cat_id):
    try:
        categoria = Categoriablog.objects.get(pk=cat_id)
    except categoriablog.DoesNotExist:
        raise Http404("La categoria ricercata non esiste.")
    context = contenuto(request)
    context.update(numpag ="3")
    context.update(cat_id=cat_id)
    return render(request,"blog/index.html", context)
