import csv
from pymongo import Connection
from bson.code import Code
import random
import pickle
from datetime import datetime
import redis
from models import rentFromDict, personFromDict, carFromDict

databaseName = "mydb"
connection = Connection()
db = connection[databaseName]
r = redis.StrictRedis()

def fill_car():
    db.cars.remove({})
    csv_data = csv.reader(file('car.csv'))
    for row in csv_data:
        db.cars.insert({"id":int(row[0]),"name":row[1],"motor":int(row[2]),"cost":int(row[3]),"firm":row[4],"description":row[5]})
    print "Done"


def fill_person():
    db.persons.remove({})
    csv_data = csv.reader(file('person.csv'))
    for row in csv_data:
        db.persons.insert({"id":int(row[0]),"name": row[1],"passport":row[2]})
    print "Done"


def fill_rent():
    db.rents.remove({})
    csv_data = csv.reader(file('rent.csv'))
    for row in csv_data:
        person = db.persons.find({"id":int(row[1])})
        car = db.cars.find({"id":int(row[2])})
        db.rents.insert({"id":int(row[0]),"person":person[0],"car":car[0],"date_take":row[3],"date_back":row[4]})

    print "Done"


def fill_database():
    fill_car()
    fill_person()
    fill_rent()

def getRentsList():
        rents = []
        rent = db.rents.find()
        for x in rent:
            rents.append(rentFromDict(x))
        return rents

def getPersons():
        players = []
        pl = db.persons.find()
        for x in pl:
            players.append(personFromDict(x))
        return players
def getCars():
        cars = []
        car = db.cars.find()
        for x in car:
            cars.append(carFromDict(x))
        return cars

def getRents():
    rows = db["rents"].find()
    return rows

def getAllCars():
    rows = db["cars"].find()
    return rows

def getAllPersons():
    rows = db["persons"].find()
    return rows


def deleteRent(number):
    rent=db.rents.find({"id":int(number)})
    key = [rent.person.id,rent.car.id]
    r.delete(key)
    db.rents.remove({"id":int(number)})

def rent_to_edit(id):
    rent_to_edit = db.rents.find({"id":int(id)})
    return rent_to_edit

def updateRent(number,person,car,date_take,date_back):
    per = db.persons.find({"id":int(person)})
    ca = db.cars.find({"id":int(car)})
    db.rents.update(
   { "id": int(number) },
   { "$set":
      {
        "person": per[0],
        "car": ca[0],
        "date_take": date_take,
        "date_back": date_back
      }
   }
)


def addRent(person,car,date_take,date_back):
    max = db.rents.aggregate({
    "$group": {
        "_id": '',
        "last": {
            "$max": "$id"
        }
    }
    })
    id = max['result'][0]["last"] + 1
    per = db.persons.find({"id":int(person)})
    ca = db.cars.find({"id":int(car)})
    db.rents.insert({"id":id,"person":per[0],"car":ca[0],"date_take":date_take,"date_back":date_back})

def getStatistics():
    map = Code("function()"
               "{"
               "    emit(this.person.name, 1);"
               "}")

    reduce = Code("function (key, values)"
                  "{"
                  "     var total = 0;"
                  "     for (var i in values)"
                  "     {"
                  "         total += values[i];"
                  "     }"
                  "     return total;"
                  "}")
    db.rents.map_reduce(map, reduce, "stat")
    results = db.stat.find()
    a = []
    for i in results:
        b = []
        b.append(str(i["_id"]))
        b.append(str(int(i["value"])))
        a.append(b)
    return a

def getStatistics1():
    map = Code("function()"
               "{"
               "    emit(this.car.firm+','+this.car.name, 1);"
               "}")

    reduce = Code("function (key, values)"
                  "{"
                  "     var total = 0;"
                  "     for (var i in values)"
                  "     {"
                  "         total += values[i];"
                  "     }"
                  "     return total;"
                  "}")
    db.rents.map_reduce(map, reduce, "stat")
    results = db.stat.find()
    a = []
    for i in results:
        b = []
        b.append(str(i["_id"]))
        b.append(str(int(i["value"])))
        a.append(b)
    return a

def generate():
    max = db.rents.aggregate({
                "$group": {
                    "_id": '',
                    "last": {
                        "$max": "$id"
                    }
                }
            })
    id = max['result'][0]["last"]
    for i in range (0,50000):
            rand_person = random.randint(0, 8)
            rand_car = random.randint(0, 9)
            person = db.persons.find().skip(rand_person).next()
            car = db.cars.find().skip(rand_car).next()
            year = random.randint(2000, 2016)
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            date_take = datetime(year, month, day)
            year1 = random.randint(2000, 2016)
            month1 = random.randint(1, 12)
            day1 = random.randint(1, 28)
            date_back = datetime(year1, month1, day1)
            id = id +1
            if date_back<date_take:
                rent = {'id':id,'person': person, 'car': car,'date_take': date_back,'date_back': date_take}
            else:
                rent = {'id':id,'person': person, 'car': car,'date_take': date_take,'date_back': date_back}
            db.rents.insert(rent)

def search(key):
        if r.exists(key) != 0:
            rents = pickle.loads(r.get(key))
        else:
            if key != '0':
                rents = list(db.rents.find({"person.id":int(key[0]),'car.id': int(key[1])}))
            r.set(key,  pickle.dumps(rents))
        new_rents = []
        for x in rents:
            new_rents.append(rentFromDict(x))
        return new_rents

def status(key):
        if r.exists(key) != 0:
            return 0
        else: return 1