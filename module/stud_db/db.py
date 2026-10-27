
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
        "semester": 3,
        "passed_exams": [
            "Programmierung",
            "BWL",
            "Datenbanken"
        ]
    }
]

def get_students():
    return students

def get_student_by_name(name):
    student = None
    # TODO
    return student

def get_students_by_country(country):
    students_filtered = []
    # TODO
    return students_filtered

def add_student(name, age, city, zip, country, street, semester, passed_exams):
    # TODO
    return "Student hinzugefügt."

def delete_student(name):
    # TODO
    return "Student gelöscht"

def go_to_next_semester(student):
    # TODO
    return "Studnet im näcshten Semester"

def add_passed_exam(name, passed_exam):
    # TODO
    return "Passed exam added"



