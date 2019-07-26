"""
Program: Zoo
Functionality:
- Register new animals
- See the list of animals
- ...
"""
from animal import Animal
animals = []

def print_menu():
    print("*" * 20)
    print(" Welcome to Zuper Zoo ")
    print("*" * 20)

    print("1 - Register new animal")
    print("2 - Count animals")
    print("3 - List the animals")

    print("x - Exit the system")

def register_animal():
    try:
        name = input("What is the animal's name?")
        species = input("What species is the animal?")
        age = int(input("How old is the animal?"))

        new_animal = Animal(name,age,species)
    

        animals.append(new_animal)

        print("***Animal registered***")
    except:
        print("*!*!*!*!*Error, verify and try again*!*!*!*!*")
    
def count_animals():
    number = len(animals)
    if(number == 1):
         print("There is " + str(number) + " animal in the zoo")
    elif(number !=1):
         print("There are " + str(number) + " animals in the zoo")

def list_animals():
    for zoo_animal in animals:
        print("name:" + zoo_animal.name,"age:" + str(zoo_animal.age),"species:" + zoo_animal.species)


opc = ""
while( opc != "x"):
    print("\n\n\n\n")
    print_menu()

    opc = input('Please select an option ')
    if(opc == "1"):
        register_animal()
    elif(opc == "2"):
        count_animals()
    elif(opc == "3"):
        list_animals()

print('_' * 20)
print("Thank you, good byte")