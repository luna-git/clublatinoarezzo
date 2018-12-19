from django.urls import path

from . import views
from home.views import index
from blog.views import clablog

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("../blog", clablog, name="blogindex"),
    path("../home", index, name="homeindex"),
]
