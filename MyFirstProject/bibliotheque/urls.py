from django.urls import path,include
from . import views

urlpatterns = [
    path('ajout/', views.ajout),
    path('traitement/', views.traitement), # ajouter la route traitement associé à l'action traitement du fichier views.py
    path('affiche/<int:id>/',views.read), # ajouter la route traitement associé à l'action traitement du fichier views.py. bien faire attention qu'il n'y ai pas d'espace dans les balises <>, sinon cela génère une erreur.
    path('update/<int:id>/',views.update),
]