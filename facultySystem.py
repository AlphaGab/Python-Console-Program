from faculty import Faculty
import os
def show_table():
    print('''Table of Faculty Rank
  Rank    Salary         Class
     1    22,000.00      D
     2    35,000.00      D
     3    33,000.00      C
     4    46,000.00      C
     5    57,000.00      B
     6    68,000.00      A
     7    73,000.00      A''')
def show_menu():
    print('''\n   -----------------------------
   Faculty Management System
   -----------------------------

   A.) Enter New Faculty Member
   B.) Search Faculty Member by Name
   C.) Search Faculty Members by Rank
   D.) Tabulate Faculty Ranks
   E.) Show All Faculty Members
   F.) Exit''')

def showAll(list):
    for i in list:
        print(str(i))

os.system('clear')
faculty1 = Faculty("gabriel", "cavite", 2, "gmail.com", 24, 105, "6'5", "brown", 225000)
faculty2 = Faculty("miguel", "cavite", 1, "gmail.com", 24, 105, "6'2", "brown", 225000)
faculty3 = Faculty("jericho", "cavite", 1, "gmail.com", 24, 105, "4'1", "brown", 225000)
facultyList = []
facultyList.append(faculty1)
facultyList.append(faculty2)
facultyList.append(faculty3)
show_menu()
while(True):
   
    choice = input("Enter your choice:").lower().strip()
    if(choice == "a"):
         os.system('clear')
         name = input("Faculty Name\t:\t")
         address = input("Faculty Address\t:\t")
         rank = int(input("Faculty Rank\t:\t"))
         email = input("Faculty Email\t:\t")
         age = input("Faculty Age\t:\t")
         weight = input("Faculty Weight\t:\t")
         height = input("Faculty Height\t:\t")
         color = input("Faculty Color\t:\t")
         salary = input("Faculty Salary\t:\t")
         faculty = Faculty(name,address,rank,email,age,weight,height,color,salary)
         facultyList.append(faculty)
         print("\tSuccessfully Added")
    elif(choice == "b"):
        os.system('clear')
        found = False
        nameQuery = input("Enter Name: ")
        for person in facultyList:
            if (person.get_name() == nameQuery):
                print(str(person))
                found = True
        if not found:
            print("Name not found")
    elif(choice == "c"):
        os.system('clear')
        rankQuery = int(input("Enter Rank: "))
        for person in facultyList:
            if (person.get_rank() == rankQuery):
                print(f"Mr/Ms. {person.get_name()} is {person.get_salary()} with Rank {person.get_rank()} and Class as {person.get_class()}")
    elif(choice == "d"):
        os.system('clear')
        show_table()
    elif(choice == "e"):
        os.system("clear")
        faculty_sorted = sorted(facultyList, key=lambda x: x.get_rank())
        showAll(faculty_sorted)
    elif(choice == "f"):
        break
    show_menu()

print("System Closed")

