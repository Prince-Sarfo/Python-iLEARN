from cmath import pi


print('Hello World')
print('o-----')
print('  ||||')
# This is the python course that I am starting with Mosh
print('*' * 10)

# Varibles in python
# We have int, floating point, boolean, string and whole lot
# Exe 1 is to print name, age of patient and tell if he is new patient or not

name = "John Smith"
age = 20
is_newPatient = True

# Getting User input
# full_name = input('What is your name? ')
# color = input('What is your favorite color? ')
# print(full_name + ' likes ' + color)

# Writing a program to calculate the our year
# year_born = input('What year were your born? ')
# age = str(2022 - int(year_born))
# print('You are ' + age + ' years old')

name = 'Jennifer'
another = name[1:-1]
print(another)

# Formatting a string
# To format a string, prefix it with an f and use the culry
# as a placeholder
first_name = "Sandra"
last_name = "Antwi"
message = f'{first_name} [{last_name}] is a coder'
print(message)

#String funtions and methods
# upper(), lower(), title(), find(), replace(), in, len()
course = "Python is the best programming language for cybersecurity"
print(len(course))
print(course.upper())
print(course.lower())
print(course.title())
print(course.replace("Python","Java"))
print("Language" in course)

# Implementing if-statements
price = 1000000
good_credit = False
if good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"down payment : ${down_payment}")

# Implementing logical operator and, or, not
# Implementing comparison operators >,<, <=,>=, !=
name = input("What is your name?")
if len(name) < 3:
    print("Name must be atleast 3 characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good!")

# Implementing a weight program to, the extended program
weight = input("Weight: ")
unit = input("(L)bs or (K)g: ").lower() 
if unit == "l":
    converted_weight = float(weight) * 0.45
    final = round(converted_weight,2)
    print(f"You are {final} kilograms")
elif unit == "k":
    converted_weight = float(weight) / 0.45
    final = round(converted_weight)
    print(f"You are {final} pounds")
else:
    print(f"You entered wrong value")

# Making a guessing game

guess_number = 9
guess_limit = 3
guess_start = 0
while guess_start < guess_limit:
    user_guess = int(input("Guess a number: "))
    guess_start += 1
    if guess_number == user_guess:
        print(f"You won!")
        break
else:
    print(f"Sorry, you lost!")


#Building a car game
menu = ""
while True:
    menu =  input("> ").lower()
    if menu == "start":
        print(f"Car started..... ready to go")
    elif menu == "stop":
        print(f"Car stopped.")
    elif menu == "help":
         print("""start - to start the car
stop - to stop the car
quit - to exit""")
    elif menu == "quit":
        break
    else:
        print(f"I don't undertand that......")

# For loop
for item in "python":
    print(item)

price = [10,20, 30]
amount = 0
for list in price:
    amount += list
print(amount)

        




