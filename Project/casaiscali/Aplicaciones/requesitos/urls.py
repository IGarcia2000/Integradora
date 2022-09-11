from django.urls import path
from . import views

urlpatterns = [
    path("servicios/", views.servicios, name = "servicios"),
    path("eventos/", views.eventos, name = "eventos"),
    path("zpsicologica/", views.zpsico, name = "zpsicologica"),
    path("designer/", views.zgrafica, name = "designer"),
]