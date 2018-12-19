from django.urls import path

from . import views
from authentication.views import index

urlpatterns = [
    path("", views.index, name="index"),
    path("index.html", views.index, name="index"),
    path("about.html", views.about, name="about"),
    path("staff.html", views.staff, name="staff"),
    path("blog.html", views.blog, name="blog"),
    path("servizi.html", views.servizi, name="servizi"),
    path("galleria.html", views.galleria, name="galleria"),
    path("contact.html", views.contact, name="contact"),
    path("contactform1.html", views.contactform1, name="contactform1"),
    path("home/login.html", index, name="login"),
]
