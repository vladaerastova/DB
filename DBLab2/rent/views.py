from django.shortcuts import render
from django.http import HttpResponseRedirect
from .Database import *



#fill_database()
def rents(request):
    rents = db.rents.find()
    persons = db.persons.find()
    cars = db.cars.find()
    if request.method == 'POST':
        return render(request, 'rent/home.html', {'response': {'persons': getAllPersons(),'persons1': getAllPersons(),'cars': getAllCars(),'cars1': getAllCars(),'rents' : getRents(),'id': request.POST['id'],'edit_rent': rent_to_edit(request.POST['id'])[0]}})


    return render(request, 'rent/home.html', {'response': {'persons': persons,'cars': cars,'rents' : rents,'persons1': getAllPersons(),'cars': getAllCars(),'cars1': getAllCars()}})

def delete_rent(request):
    if request.method == "POST":
        deleteRent(request.POST["id"])
        return HttpResponseRedirect('/')

def add_rent(request):
    if request.method == "POST":
        print request.POST["person_name"]
        addRent(request.POST["person_name"],request.POST["car_name"],request.POST["date_take"],request.POST["date_back"])
        return HttpResponseRedirect('/')


def edit_rent(request):
    if request.method == "POST":
        updateRent(request.POST['id'],request.POST["person_id"],request.POST["car_id"],request.POST["date_take"],request.POST["date_back"])
        return HttpResponseRedirect('/')

def persons(request):
    return render(request, 'rent/persons.html',  {'response': {'persons': getAllPersons()}})

def cars(request):
    return render(request, 'rent/cars.html',  {'response': {'cars':getAllCars(),'type':type}})

def statistics(request):
    return render(request, 'rent/statistics.html',  {'response': {'stat':getStatistics(),'stat1':getStatistics1()}})