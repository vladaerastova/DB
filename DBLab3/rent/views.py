from django.shortcuts import render
from django.http import HttpResponseRedirect
from .Database import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import time



#fill_database()
#generate()
def rents(request):
    msgs =""
    stat= ""
    key = []
    if('person_id' in request.GET and request.GET['person_id'] != '0'):
        key.append(request.GET['person_id'])
        key.append(request.GET['car_id'])
        print key

        if status(key) == 0:
            stat =  "using cash"
        else: stat = "without cash"

        start_time = time.time()
        rentsList = search(key)
        time_res = time.time() - start_time
        msgs = str(time_res)
        print status(key)
    else:
        rentsList = getRentsList()

    persons = getPersons()
    cars = getCars()
    paginator = Paginator(rentsList, 25)  # Show per page
    page = request.GET.get('page')
    try:
        rents = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        rents = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        rents = paginator.page(paginator.num_pages)

    return render(request, 'rent/home.html', {'status': stat, 'msgs': msgs, 'list': rents,
                                              'persons': persons,'cars':cars, 'total': str(len(rentsList),)})

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

def add_edit(request):
    rents = db.rents.find()

    persons = db.persons.find()
    cars = db.cars.find()

    if request.method == 'POST':
        return render(request, 'rent/add_edit.html', {'response': {'persons': getAllPersons(),'persons1': getAllPersons(),'cars': getAllCars(),'cars1': getAllCars(),'rents' : getRents(),'id': request.POST['id'],'edit_rent': rent_to_edit(request.POST['id'])[0]}})

    return render(request, 'rent/add_edit.html', {'response': {'persons': persons,'cars': cars,'rents' : rents,'persons1': getAllPersons(),'cars': getAllCars(),'cars1': getAllCars()}})