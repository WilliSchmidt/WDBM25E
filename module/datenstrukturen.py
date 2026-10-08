# Datenstrukturen: Strukturieren von Daten


# LISTEN:
# vordefinieren / anlegen:
l = [1, 2, 3]  # Eine Liste mit 3 Elementen
#    0, 1, 2

l2 = []

# manipulieren:
l[1] = "hallo"

# auslesen:
print(l[1])  # gebe mir das Element mit dem Index 1 der Liste L aus

# löschen:
del l[1]
print(l)

# Elemente dranhängen:
l.append("welt")
print(l)


# TUPLE:
t = tuple((59, 10))
print(t[0])


# DICTS: JSON
# anlegen:
d = {
    # key :  value
    "Willi": "012456789",
    "Andreas": "015745152151",
    "Paul": "01574234355152151"
}
print(d)

# auslesen:
print(d["Andreas"])

# löschen:
del d["Andreas"]

# manipulieren:
d["Paul"] = "012312121212"

# Olaf 01112221148 mit in die Liste aufnehmen:
d["Olaf"] = "01112221148"

print(d)





# Beispiel: Verschachtelung

students = [
    {
        "name": "Willi",
        "age": 38,
        "address": {
            "city": "Stuttgart-Sillenbuch",
            "zip": "70619",
            "country": "USA",
            "street": "Hauptstraße 26"
        },
        "Semester": 3,
        "bestande Vorelsungen": [
            "Programmierung",
            "BWL",
            "Datenbanken"
        ]
    },
    {
        "name": "Andreas",
        "age": 49,
        "address": {
            "city": "Fellbach",
            "zip": "324243",
            "country": "USA",
            "street": "Hauptstraße 1"
        },
        "Semester": 5,
        "bestande Vorelsungen": [
            "BWL"
        ]
    },
]

# Olaf, 19, Stuttgart, 70469, DE, Hauptstraße 12, 1
students.append({
    "name": "Olaf",
    "age": 19,
    "address": {
        "city": "Stuttgart",
        "zip": "70469",
        "country": "DE",
        "street": "Hauptstraße 12"
    },
    "Semester": 1,
    "bestande Vorelsungen": []
})

print(students)
print(students[1]["name"] == "Andreas")
print(students[1]["age"])

# wie bekomme ich die PLZ von Olaf?
print(students[2]["address"]["zip"])


# Olaf besteht das erste Semester mit folgenden Vorlesungen: "BWL", "Programmierung"
students[2]["Semester"] = students[2]["Semester"] + 1
students[2]["bestande Vorelsungen"].append("BWL")
students[2]["bestande Vorelsungen"].append("Programmierung")

print(students)

# Olaf wird exmatrikuliert:
del students[2]
print(students)

# Olaf zieht um. neue adresse Köln, 123243, DE, Hauptksdflk 12
students[2]["address"]["zip"] = "12324"
students[2]["address"]["city"] = "Köln"
students[2]["address"]["country"] = "DE"
students[2]["address"]["street"] = "Hauptksdflk 12"
print(students)















