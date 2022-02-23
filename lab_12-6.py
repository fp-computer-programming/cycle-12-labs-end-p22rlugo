# Ryan Lugo: RJL 02/23/22

grades = {"Start S2 Labs":0,"End S1 Labs":100,"Mid-year Project Proposal":90,"Cycle 10 Practice Quiz":100,"Cycle 10 Quiz":93}


print(grades)

for k,v in grades.items():
    print(k)

for k,v in grades.items():
    if v >= 70:
        print("You got a",v,"on",k)

for k,v in grades.items():
    if v <= 50:
        print("You got a",v,"on",k)