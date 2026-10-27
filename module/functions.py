def add(a, b):
    summe = a + b
    return summe

def subtract(a, b):
    return a - b

c = add(1, 2)
print(c)
d = subtract(3, 4)
print(d)


# Programmiere ein Funktion bmi (Body-Maß-Index) und teste.
# bmi = w / (s * s)

def calculate_bmi(w, s):
    bmi = w / (s * s)  # s**2
    return bmi

w = input("Gewicht in kg: ")
s = input("Größe in m: ")
c = calculate_bmi(float(w), float(s))
print(c)
