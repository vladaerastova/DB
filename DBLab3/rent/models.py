from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person:
    def __init__(self, id, name, passport):
        self.Id = id
        self.Name = name
        self.Passport = passport


def personFromDict(dict):
    person = Person(dict['id'], dict['name'], dict['passport'])
    return person

class Rent:
    def __init__(self, id, person, car,date_take,date_back):
        self.Id = id
        self.Person = person
        self.Car = car
        self.Date_Take = date_take
        self.Date_Back = date_back


def rentFromDict(dict):
    rent = None
    if dict != None:
        rent = Rent(dict['id'], personFromDict(dict['person']), carFromDict(dict['car']),
                              dict['date_take'], dict['date_back'])
    return rent

class Car:
    def __init__(self,id, name,firm,description,cost, motor):
        self.Id = id
        self.Name = name
        self.Firm = firm
        self.Description = description
        self.Cost = cost
        self.Motor = motor


def carFromDict(dict):
    car = Car(dict['id'], dict['name'], dict['firm'], dict['description'], dict['cost'], dict['motor'])
    return car