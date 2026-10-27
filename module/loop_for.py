
students = [
    ["willi@dhbw.de", "1234"],
    ["andreas@dhbw.de", "abcd"],
    ["paul@dhbw.de", "9876"],
]
while True:
    email = input("Enter your email: ")
    pwd = input("Enter your password: ")
    logged_in = False
    for student in students:
        if student[0] == email and student[1] == pwd:
            logged_in = True
            break

    if logged_in:
        print("du bist eingeloggt :)")
    else:
        print("du bist nicht eingeloggt:(")
        break

