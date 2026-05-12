from django.shortcuts import render
from .forms import LivreForm
from . import models

def ajout(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après une saisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = LivreForm(request)
        if form.is_valid(): # validation du formulaire.
            Livre = form.save() # sauvegarde dans la base
            return render(request,"bibliotheque/affiche.html",{"Livre" : Livre}) # envoie vers une page d'affichage du Livre créé
        else:
            return render(request,"bibliotheque/ajout.html",{"form": form})

    else :
        form = LivreForm() # création d'un formulaire vide
        return render(request,"bibliotheque/ajout.html",{"form" : form})


def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save()
        return render(request,"bibliotheque/affiche.html",{"Livre" : Livre})
    else:
        return render(request,"bibliotheque/ajout.html",{"form": lform})

def read(request, id):
    Livre = models.Livre.objects.get(pk=id) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"bibliotheque/affiche.html",{"Livre": Livre})

def update(request, id):
    livre = Livre.objects.get(id=id)
    lform = LivreForm(dictionnaire) # ou le dictionnaire est celui qui contient toutes les valeurs


