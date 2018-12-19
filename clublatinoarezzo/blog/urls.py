from django.urls import path

from . import views
from authentication.views import index

urlpatterns = [
    path("", views.clablog, name="clablog"),
    path("index.html", views.clablog, name="clablog"),
    path("<int:art_id>", views.clablog_id, name="clablog_id"),
    path("c<int:cat_id>", views.clablog_cat, name="clablog_cat"),
    path("login.html", index, name="login"),
]
