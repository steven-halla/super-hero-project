from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero
# Create your views here.

def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
    hero = Superhero.objects.get(pk=hero_id)
    context = {
        'hero': hero
    }
    return render(request, 'superheroes/detail.html', context)

def create(request):
    if request.method == "POST":
        print("Hit with Post")
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_abilith=secondary, catch_phrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

def update(request, hero_id):
    hero = Superhero.objects.get(pk=hero_id)
    context = {
        'hero': hero
    }
    print("hero " + str(hero))
    if request.method == "POST":
        print("Hit with PUT")

        hero.name = request.POST['name']
        hero.alter_ego = request.POST['alter_ego']
        hero.primary = request.POST['primary']
        hero.secondary = request.POST['secondary']
        hero.catchphrase = request.POST['catchphrase']
        hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/update.html', context)

def delete(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    single_hero.delete()

    return HttpResponseRedirect(reverse('superheroes:index'))
