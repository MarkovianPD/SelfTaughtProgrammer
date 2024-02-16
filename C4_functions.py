def f(x):
    return x * 2


result = f(2)
print(result)


def f(x):
    return x + 1


z = f(4)

if z == 5:
    print("z is 5")
else:
    print("z is not 5")


def f():
    return 1 + 1


result = f()
print(result)


def f(x, y, z):
    return x + y + z


result = f(1, 2, 3)
print(result)


def f():
    z = 1 + 1


result = f()
print(result)

len("Monty")
len("Python")
str(100)
int("1")
float(100)
int("110")
int(20.54)
float("16.4")
float(99)

# int("Prince") ValueError: invalid literal for int() with base 10: 'Prince'

age = input("Enter your age:")
int_age = int(age)
if int_age < 21:
    print("You are young!")
else:
    print("Wow, you are old!")


def even_odd(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")


even_odd(2)
even_odd(3)


def even_odd_input():
    n = input("Type a number: ")
    n = int(n)
    if n % 2 == 0:
        print("n is even.")
    else:
        print("n is odd.")


even_odd_input()
even_odd_input()
even_odd_input()


def f(x=2):
    return x ** x


print(f())
print(f(4))


def add_it(x, y=10):
    return x + y


result = add_it(2)
print(result)

x = 1
y = 2
z = 3


def f():
    print(x)
    print(y)
    print(z)


f()

a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)
print(a / b)
try:
    print(a / b)
except ZeroDivisionError:
    print("Can't divide by zero.")

try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("Invalid input.")
