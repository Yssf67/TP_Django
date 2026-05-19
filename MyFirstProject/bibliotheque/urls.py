from django.urls import path,include
from . import views, categorie_views

urlpatterns = [
    path("", views.index),
    path("ajout/", views.ajout),
    path("traitement/", views.traitement),
    path("affiche/<int:id>/", views.read),
    path("update/<int:id>/", views.update),
    path("traitementupdate/<int:id>", views.traitementupdate),
    path("delete/<int:id>/", views.delete),
    #pages pour les categories
]