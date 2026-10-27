
students = [
    ["willi@dhbw.de", "1234"],
    ["andreas@dhbw.de", "abcd"],
    ["paul@dhbw.de", "9876"],
]
i = 0
while i < 3:
    email = input("Enter your email: ")
    pwd = input("Enter your password: ")
    logged_in = False
    for student in students:
        if student[0] == email and student[1] == pwd:
            logged_in = True
            break
    i = i + 1
    if logged_in:
        print("du bist eingeloggt :)")
    else:
        print("du bist nicht eingeloggt:(")
if i == 3:
    print("du bist gesperrt!!!!!!!!")

