from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Animaux, Equipement


def index(request):
    animaux_list = Animaux.objects.all()
    template = loader.get_template('animalerie/index.html')
    context = {
        'animaux_list': animaux_list,
    }
    return HttpResponse(template.render(context, request))

def manage(request, id):
    animal = get_object_or_404(Animaux, pk=id)
    context = {
        'animal': animal,
    }
    template = loader.get_template('animalerie/manage.html')
    return HttpResponse(template.render(context, request))

def nourrir(request,id):
    animal = get_object_or_404(Animaux, pk=id)
    mangeoire = Equipement.objects.get(id=4)
    safe = animal.animal_lieu
    if mangeoire.disponibilite == 1 :
        return HttpResponse('Impossible : le mangeoire est occupé')
    if animal.animal_etat == 'Affamé' :
        animal.animal_lieu = mangeoire
        animal.animal_etat = 'Repus'
        mangeoire.disponibilite = 1
        safe.disponibilite = 0
        safe.save()
        mangeoire.save()
        animal.save()
        return HttpResponse('Vous avez nourri %s.' % animal.animal_id)
    return HttpResponse('Impossible : l animal n a pas faim')

def faire_exercice(request,id):
    animal = get_object_or_404(Animaux, pk=id)
    roue = Equipement.objects.get(id=2)
    safe = animal.animal_lieu
    if roue.disponibilite == 1 :
        return HttpResponse('Impossible : la roue est occupé')
    if animal.animal_etat == 'Repus':
        animal.animal_lieu = roue
        animal.animal_etat = 'Fatigué'
        roue.disponibilite = 1
        safe.disponibilite = 0
        safe.save()
        roue.save()
        animal.save()
        return HttpResponse('Vous avez diverti %s.' % animal.animal_id)
    return HttpResponse('Impossible : l animal n est pas repus')

def reveiller(request,id):
    animal = get_object_or_404(Animaux, pk=id)
    littiere = Equipement.objects.get(id=1)
    safe = animal.animal_lieu
    if littiere.disponibilite == 1:
        return HttpResponse('Impossible : le littiere est occupé')
    if animal.animal_etat == 'Endormi':
        animal.animal_lieu = littiere
        animal.animal_etat = 'Affamé'
        safe.disponibilite = 0
        safe.save()
        littiere.save()
        animal.save()
        return HttpResponse('Vous avez réveillé %s.' % animal.animal_id)
    return HttpResponse('Impossible : l animal n est pas endormi')

def faire_dormir(request,id):
    animal = get_object_or_404(Animaux, pk=id)
    nid = Equipement.objects.get(id=3)
    safe = animal.animal_lieu
    if nid.disponibilite == 1:
        return HttpResponse('Impossible : le nid est occupé')
    if animal.animal_etat == 'Fatigué':
        animal.animal_lieu = nid
        animal.animal_etat = 'Endormi'
        nid.disponibilite = 1
        safe.disponibilite = 0
        safe.save()
        nid.save()
        animal.save()
        return HttpResponse('Vous avez endormi %s.' % animal.animal_id )
    return HttpResponse('Impossible : l animal n est pas fatigué')









