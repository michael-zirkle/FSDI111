
def say_hello():
    print("I'm a function")

def perform_sum(num1, num2):
    print("performing sum operation inside a function")
    return num1 + num2

# perform_div

def perform_div(num1, num2):
    if(num2 == 0):
        print("error cannot divide by 0")
        return 0
    print("performing division operation")
    return num1 / num2

print("*" * 20)
print(" Wlecome to my Calculator ")
print("*" * 20)

num1 = input("Please provide num1: ")
num2 = input("Please provide num2: ")

f_num1 = float(num1)
f_num2 = float(num2)

say_hello()
res = perform_sum(f_num1, f_num2)
print("Sum result " + str(res))

say_hello()
res2 = perform_div(f_num1, f_num2)
print("Division reslult " + str(res2))

print("*" * 20)

for i in range(10): # for i=0; i < 10; i++
    print(i)

fruits = ["apple", "orange", "bannana", "strawberry"]
print(fruits)
print(fruits[0])

print("with a for loop")

for fruit in fruits:
    print(fruit)

opc = ''
while(opc !="x"):
    #print some menu here
    opc = input("Select an option")
