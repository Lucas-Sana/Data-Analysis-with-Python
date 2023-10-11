import random
from decimal import Decimal

def add_numbers(x, y):
    return x + y

name = "Mary"
age = 30
print(name)
print(age)
print(name, "is", age, "years old")

# Data Types
# Integers, type int:
age = 30

# Floats, type float:
price = 2.50

# Strings, type str
print("Hello unicode 👋")
print('Omelette Du Fromage 🧀')

# Booleans, type bool
True

# None, type NoneType
x = None
print(x)
print(type(None))

# int, float, str and bool objects and functions
age_as_string = "28"
int(age_as_string)
age = int(age_as_string)
type(age)
type(13) == int

# Functions
def hello():
    return "Hello World"

result = hello()
result

def add(x, y):
    return x + y

add(2, 3)

def add(*args):
    return sum(args)

add(1, 1, 1)
add(1)

# Operators
3 + 3
11 % 7
2 ** 4
3 + 4 * 5

# Boolean operators
7 > 3
8 >= 8
True and True
not False
False or True

# Control Flow
days_subscribed = 28

if days_subscribed >= 30:
    print("Loyal customer")
elif days_subscribed >= 15:
    print("Halfway there")
elif days_subscribed >= 1:
    print("Building confidence")
else:
    print("Too early")

# For loops
names = ['Monica', 'Ross', 'Chandler', 'Joey', 'Rachel']

for name in names:
    print(name)

# While loops
count = 0

while count < 3:
    print("Counting...")
    count += 1

# Collections
l = [3, 'Hello World', True]
len(l)
l[0]
l[1]
l[-1]
l[-2]
l.append('Python 🐍')
'Python 🐍' in l

t = (3, 'Hello World', True)
t[0]
t[-1]
'Hello World' in t

user = {
    "name": "Mary Smith",
    "email": "mary@example.com",
    "age": 30,
    "subscribed": True
}
user['email']
'age' in user
'last_name' in user

s = {3, 1, 3, 7, 9, 1, 3, 1}
s.add(10)
s.pop()

# Iterating collections
for elem in l:
    print(elem)

for key in user:
    print(key.title(), '=>', user[key])

# Modules
random.randint(0, 99)

# Exceptions
try:
    if age > 21:
        print("Allowed entrance")
except TypeError:
    print("Age is probably of a wrong type")

# We're just getting started
# ... (More content is here but not included in this response)
