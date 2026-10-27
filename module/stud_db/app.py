from module.stud_db import db

print(db.get_students())

db.add_student(
    "Olaf",
    22,
    "Stuttgart",
    "70649",
    "USA",
    "Hauptstraße 33",
    5,
    ["BWL"]
)

print(db.get_students())


