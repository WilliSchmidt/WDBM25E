# IF Konstrukte:

email = input("Email: ")
pw = input("Passwort: ")

if email == "willi@dhbw.de":
    if pw == "1234":
        print("Eingeloggt :)")
    else:
        print("Einloggen fehlgeschlagen :(")
elif email == "olaf@dhbw.de": # elif steht für ELSE + IF  ( ansonsten wenn)
    if pw == "1111":
        print("Eingeloggt :)")
    else:
        print("Einloggen fehlgeschlagen :(")
elif email == "andreas@dhbw.de":
    if pw == "aaa":
        print("Eingeloggt :)")
    else:
        print("Einloggen fehlgeschlagen :(")
else:
    # False-Block
    print("Einloggen fehlgeschlagen :(")
