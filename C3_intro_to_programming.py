import math

# This is a comment
print("Hello, World!")

# print Hello!, World! | Useless comment
print("Hello, World!")

# Calculate the length of a diagonal of a rectangle | Useful comment
l = 4
w = 10
d = math.sqrt(1**2 + w**2)
print(d)

print("Python")

print("Hola!")

print("""This is a really really
    long line of 
    code.""")

print\
    ("""This is a really really
    really long line of code.""")

for i in range(100):
    print("Hello, World!")

b = 100
print(b)

home = "America"
if home == "America":
    print("Hello, America!")
else:
    print("Hello, World!")

home = "Canada"
if home == "America":
    print("Hello, America!")
else:
    print("Hello, World!")

x = 2
if x == 2:
    print("The number is 2.")
if x % 2 == 0:
    print("The number is even.")
if x % 2 != 0:
    print("The number is odd.")

x = 10
y = 11

if x == 10:
    if y == 11:
        print(x + y)

home = "Thailand"
if home == "Japan":
    print("Hello, Japan!")
elif home == "Thailand":
    print("Hello, Thailand!")
elif home == "India":
    print("Hello, India!")
elif home == "China":
    print("Hello, China!")
else:
    print("Hello, World!")

home = "Mars"
if home == "America":
    print("Hello, America!")
elif home == "Canada":
    print("Hello, Canada!")
elif home == "Thailand":
    print("Hello, Thailand!")
elif home == "Mexico":
    print("Hello, Mexico!")
else:
    print("Hello, World!")

x = 100
if x == 10:
    print("10!")
elif x == 20:
    print("20!")
else:
    print("I don't know!")

if x == 100:
    print("x is 100!")

if x % 2 == 0:
    print("x is even!")
else:
    print("x is odd!")

"""
Challenges:
1. Print three difference strings.
2. Write a program that prints a message if a variable is less than 10, and different message if the variable is greater than 10.
3. Write a program that prints a message if a variable is less than or equal to 10, another message if the variable is greater than 10 but less than or equal to 25, and another message if the variable is greater than 25.
4. Create a program that divides two variables and prints the remainder.
5. Create a program that takes two variables, divides them, and prints the quotient.
6. Write a program with a variable age assigned to an integer that prints different strings depending on what integer age is.
"""

# Challenge 1
print("String 1")
print("String 2")
print("String 3")

# Challenge 2
num = 10
if num < 10:
    print("Your number is 10!")
else:
    print("Your number is not 10!")

# Challenge 3
num = 24
if num <= 10:
    print("Your number is less than or equal to 10!")
elif num <= 25:
    print("Your number is greater than 10, but less than or equal to 25!")
else:
    print("Your number is greater than 25!")

# Challenge 4
x = 10
y = 3
print(x % y)

# Challenge 5
print(x // y)

# Challenge 6
age = 26
if age >= 15 and age <= 17:
    print("You probably have your permit to drive!")
elif age >= 18 and age <= 20:
    print("You're an adult now and probably have your drivers license!")
elif age >= 21 and age <= 24:
    print("Congratulations you're able to drink now!")
elif age == 25:
    print("Congratulations you can rent a jet ski now!")
else:
    print("Sorry, you are old.")