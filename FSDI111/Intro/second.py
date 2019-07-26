print("******************")
print('   WELCOME      ')
print("---------------------")

age = input('Please type your age: ')

#print(age)
#print(type(age))
the_age = int(age) #convert(parse) the string into int
print(the_age + 1)

# Operations with string variables

name = input("Please tell me your name: ")

print("Welcome: " + name )
name_length = len(name) # len() gives length of string in array
print('Your name has ' + str(name_length) + ' letters')

print(name.upper()) # to upper case
print(name.lower()) # to lower case
print(name.replace('M','Z'))

has_E = "e" in name # true or false
print("Your anem contains e: " + str(has_E))

print('_' * 20)
pet = input('What pet do you have? ')

if (pet == 'Lion'):
    print('Well done!')
elif(pet == 'Cat'):
    print('Getting there')
else:
    print("Get a Lion")