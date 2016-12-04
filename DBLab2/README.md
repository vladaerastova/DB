Author: Yerastova Vlada 

Завдання роботи полягає у наступному:

1.Розробити схему бази даних на основі предметної галузі з ЛР№2-Ч1 у спосіб, що застосовується в СУБД MongoDB.

2.Розробити модуль роботи з базою даних на основі пакету PyMongo.

3.Реалізувати дві операції на вибір із використанням паралельної обробки даних Map/Reduce.

4.Реалізувати обчислення та виведення результату складного агрегативного запиту до бази даних з використанням функції aggregate() сервера MongoDB.

Тексти функції Map/Reduce та aggregate():
max = db.rents.aggregate({
    "$group": {
        "_id": '',
        "last": {
            "$max": "$id"
        }
    }
    })

ef getStatistics():
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


