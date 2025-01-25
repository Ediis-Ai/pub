print("Course Registration Simulation:\nExplanation: You play the role of 5 students, an education manager, and a teacher")

droos = {"farsi": 5, "riazi": 5, "zaban": 5, "dini": 5, "hesanban": 5, "hendese": 2, "fizik": 1}
users = {"ali":["farsi" ,"riazi" , "dini"], "reza":["dini" , "farsi", "hendese"]}
os = ["farsi","riazi","tarikh","zaban"]

def md():
    global users, droos, oss

    print("You are the education manager. First, view the list of courses and their capacities.")

    for key, vl in droos.items():
        print(f"Course: {key} has {vl} capacity")

    print("Please increase or decrease the capacity of one of the courses.")
    print("First, you must send the capacity of the courses. If your course is not in the list, it will be added.")
    print("In the form: farsi 15 zaban 2 and ....")
    print("If you want to delete a course, set its capacity to - : farsi -")
    

md()

def rem():
    global droos

    while True:
        inp = [x.lower() for x in input().split()]
        if len(inp) % 2 == 0 and not inp[0].isdigit():
            for i in range(0, len(inp), 2):
                if inp[i + 1] == "-":
                    del droos[inp[i]]
                    print(f"Course {inp[i]} has been deleted")
                else:
                    droos[inp[i]] = int(inp[i + 1])
                    print(f"Capacity of course {inp[i]} changed to {inp[i + 1]}")
            break
        else:
            print("Invalid input")
    print("New list:")
    for key, vl in droos.items():
        print(f"Course: {key} has {vl} capacity")
        

rem()

def endterm():
    global droos, users

    for i in range(1, 6):
        print(f"You are currently student number {i}. Select 5 units from the following courses.")
        for ky, vl in droos.items():
            print(f"Course: {ky} has {vl} capacity")

        valid_selection = False
        while not valid_selection:
            print("Please send the names of your courses separated by spaces: (farsi riazi, ....)")
            inp = [str(x) for x in input().split()]
            if len(inp) == 5:
                valid_selection = True
                for dr in inp:
                    if dr in droos:
                        if droos[dr] > 0:
                            valid_selection = True
                        else:
                            print(f"Course {dr} is full")
                            valid_selection = False
                            break
                    else:
                        print(f"Course: {dr} is not in the list")
                        valid_selection = False
                        break
                    if valid_selection:
                        users[str(i)] = inp
                        droos[dr] -= 1
                        print(users)
            else:
                print("Please enter 5 courses")

endterm()

def dh():
    print("You are now the education manager again. You can add or remove courses for students.")
    print("Currently, you are viewing the list of students.")

    for key, valu in users.items():
        print(f"Student {key} has courses: {' '.join(valu)}")
    print("Enter the name of one of the students:")

    while True:
        inp = input().lower().strip()
        if inp in users:
            print("User exists. Add or remove a course.")
            onp = inp
            break
        else:
            print("User does not exist. Try again.")

    a = False
    print("If you send the course with -, it will be removed from the student's courses, and if with +, it will be added.")
    print("farsi - zaban +")

    while not a:
        b = False
        c = False
        inp = [x.lower() for x in input().split()]
        if len(inp) % 2 == 0 and not inp[0].isdigit():
            for i in range(0, len(inp), 2):

                if inp[i + 1] == "-":
                    if inp[i] in users[onp]:
                        b = True
                        a = True
                    else:
                        print("User did not have this course before")                     
                        a = False
                        b = False
                   
                if inp[i + 1] == "+":
                    if inp[i] not in users[onp]:
                        a = True
                        c = True
                    else:
                        print("User already has this course")
                        a = False
                        c = False

                if b :
                    users[onp].remove(inp[i]) 
                if c :
                    users[onp].append(inp[i])

            print(f"User {onp} has courses: {' '.join(users[onp])}")
        else:
            print("Invalid input")
            a = False
    

dh()

def fg():
    print("You are the teacher. Your class list is as follows:")
    print(f"{' '.join(os)}\nYour students are:")
    for key, vl in users.items():
        a = [x for x in os if x in vl]
        print(f"Student {key} has courses: {' '.join(a)}")

fg()