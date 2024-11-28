# Python Fundamentals

## Table of Contents
- [Variables](#variables)
   * [Handling multiple variables](#handling-multiple-variables)
   * [Check type](#check-type)
   * [Cast variables](#cast-variables)
- [Strings](#strings)
   * [Concatenate](#concatenate)
   * [Arguments by position](#arguments-by-position)
   * [Arguments by name](#arguments-by-name)
   * [F-Strings](#f-strings)
   * [String Methods](#string-methods)
- [Lists](#lists)
   * [Using a constructor](#using-a-constructor)
   * [Adding and removing](#adding-and-removing)
- [Tuples](#tuples)
   * [Using a constructor](#using-a-constructor-1)
   * [Initialising a tuple with only one element](#initialising-a-tuple-with-only-one-element)
- [Sets](#sets)
   * [Using a constructor](#using-a-constructor-2)
   * [Checking for inclusion](#checking-for-inclusion)
   * [Adding, removing and clearing](#adding-removing-and-clearing)
   * [Deleting](#deleting)
- [Dictionaries](#dictionaries)
   * [Using a constructor](#using-a-constructor-3)
   * [Accessing elements](#accessing-elements)
   * [Adding a key value pair](#adding-a-key-value-pair)
   * [Get keys and values](#get-keys-and-values)
   * [Make a copy](#make-a-copy)
   * [Removing and clearing](#removing-and-clearing)
   * [List of dictionaries](#list-of-dictionaries)
- [Functions](#functions)
   * [Lamda Functions](#lamda-functions)
- [Conditionals](#conditionals)
   * [Membership operators](#membership-operators)
   * [Identity Operators](#identity-operators)
- [Loops](#loops)
   * [For in Loops](#for-in-loops)
   * [For Range Loops](#for-range-loops)
   * [While Loops](#while-loops)
- [Modules](#modules)
   * [Core Modules](#core-modules)
   * [Installing packages](#installing-packages)
   * [Importing a custom modules](#importing-a-custom-modules)
- [Classes](#classes)
   * [Defining and instantiating classes](#defining-and-instantiating-classes)
   * [Extending classes and overwriting methods](#extending-classes-and-overwriting-methods)
- [File Manipulations](#file-manipulations)
   * [Creating and writing into files](#creating-and-writing-into-files)
   * [Appending to a file](#appending-to-a-file)
   * [Reading a file](#reading-a-file)
- [Working with JSON](#working-with-json)
   * [JSON to dictionary](#json-to-dictionary)
   * [dictionary to JSON](#dictionary-to-json)

## Variables
Different types of variables in Python:
1. int
2. float
3. string
4. bool

### Handling multiple variables
```python
x, y, name, is_cool = (1, 2.5, 'Anand', True)
print(x, y, name, is_cool)
```

### Check type
```python
print(type(y))
```

### Cast variables
```python
x = str(x)
```

## Strings
name = 'Brad'

### Concatenate
```python
name = 'Brad'
age = 37
print('Hello I am ' + name + '. I am ' + str(age))
```
If we dont cast the int, we get the TypeError

### Arguments by position
```python
print('Hello I am {1}. I am {0}.'.format(age, name))
```
Indices are optional

### Arguments by name
```python
print('Hello I am {name}. I am {age}.'.format(name=name, age=age))
```

### F-Strings
```python
print(f'Hello I am {name}. I am {age}.')
```

### String Methods
```python
s = 'heLLo THere worLD'
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.replace('worLD', 'everyone'))
print(s.count('e'))
print(s.startswith('heLLo'))
print(s.endswith(' worLD'))
print(s.split())
print(s.find('TH'))
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())
```

## Lists
Ordered and mutable collection which allows duplicate members
```python
numbers = [1,2,3,4,5]
print(type(numbers))
print(numbers)
```

### Using a constructor
```python
names = list(('Jibin', 'Allen', 'Milan', 'Anand'))
print(names)
```

### Adding and removing
```python
names.append('Anu')
names.remove('Anand')
names.insert(2, 'Anna')
names.pop(3)
names.reverse()
names.sort()
names.sort(reverse=True)
```

## Tuples
A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
```python
fruits = ('Apple', 'Orange', 'Mango')
print(fruits)
```

### Using a constructor
```python
bikes = tuple(('bmw', 'ducati', 'honda', 'yamaha'))
print(bikes)
```

### Initialising a tuple with only one element
```python
cars = ('mahindra')
print(cars)
print(type(cars))
cars = ('mahindra',)
print(cars)
print(type(cars))
```

## Sets
A Set is a collection which is unordered and unindexed. No duplicate members.
```python
gender = {'male', 'female'}
print(gender)
```

### Using a constructor
```python
directions = set(('N', 'E', 'W', 'S', 'E', 'W'))
print(directions)
```

### Checking for inclusion
```python
print('N' in directions)
```

### Adding, removing and clearing
```python
directions.add('NW')
directions.remove('E')
directions.clear()
```

### Deleting
```python
del directions
```

## Dictionaries
A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
```python
person = {
    'first_name': 'Anand',
    'last_name': 'Cherian',
    'age': 30
}
```

### Using a constructor
```python
person = dict(first_name='John', last_name='Doe', age=28)
```

### Accessing elements
```python
print(person['first_name'])
print(person.get('last_name'))
```

### Adding a key value pair
```python
person['phone'] = 10110101
```

### Get keys and values
```python
print(person.keys())
print(person.values())
```
These return a view object

### Make a copy
```python
person_two = person.copy()
```

### Removing and clearing
```python
del(person['age'])
person.pop('phone')
person.clear()
```

### List of dictionaries
```python
people = [
    {
        'name': 'Martha',
        'age': 40
    }, 
    {
        'name': 'Jane',
        'age': 29
    }
]
print(people[1]['name'])
```

## Functions

### Lamda Functions
A lambda is an anonymous function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
```python
get_sum = lambda num1, num2 : num1 + num2
print(get_sum(3,5))
increment = lambda num : num + 1
print(increment(6))
```

## Conditionals

### Membership operators
Membership operators are used to test if a sequence is presented in an object
```python
numbers = [1,2,3,4,5]
x = 6
y = 3
if x in numbers:
    print(x + ' is in numbers')
if y not in numbers:
    print(y + ' not in numbers')
```

### Identity Operators
Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
```pyton
if x is y:
    print(x is y)
if x is not y:
    print(x is not y)
```

## Loops

### For in Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string
```python
people = ['John', 'Janet', 'Karen', 'Collin']
for person in people:
    if person == 'Janet':
        continue
    if person == 'Collin':
        break
    print(person)
```

### For Range Loops
```python
for i in range(len(people)):
    print(people[i])
for i in range(0, 10):
    print(i)
```

### While Loops
While loops execute a set of statements as long as a condition is true
```python
count = 0
while count <= 10:
    print(count)
    count += 1
```

## Modules

### Core Modules
Importing the whole module
```python
import datetime
today = datetime.date.today()
print(today)
```
Taking only what we need
```python
from datetime import date
today = date.today()
print(today)
```

### Installing packages
```console
py -m venv .venv
source .venv/Scripts/activate
pip install camelcase
pip freeze
```
```python
import camelcase

camel = camelcase.CamelCase()
str = 'Hello there world'
print(camel.hump(str))
```

### Importing a custom modules
```python
from validator import validate_email

email = 'test#test.com'
if validate_email(email):
    print('email is valid')
else:
    print('not an email')
```

## Classes

### Defining and instantiating classes
```python
class User:

    def __init__(self, name, email, age) -> None:
        self.name = name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f"My name is {self.name} and I am {self.age} years old"
    
    def has_birthday(self):
        self.age += 1

brad = User('Anand', 'anand@gmail.com', 28)
print(brad.name)

brad.age = 29
print(brad.age)

brad.has_birthday()

print(brad.greeting())
```

### Extending classes and overwriting methods
```python
class Customer(User):

    def __init__(self, name, email, age) -> None:
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    # overwriting methods
    def greeting(self):
        return f"My name is {self.name} and I am {self.age} years old and I have a balance of {self.balance}"

john = Customer('John', 'john@gmail.com', '40')
print(john.balance)

john.set_balance(4000000)
print(brad.greeting())
print(john.greeting())
```

## File Manipulations

### Creating and writing into files
```python
my_file = open('myfile.txt', 'w')

print('Name: ', my_file.name)
print('Is closed: ', my_file.closed)
print('Opening mode: ', my_file.mode)

my_file.write('I love python')
my_file.write(' and JavaScript')
my_file.close()
```

### Appending to a file
```python
my_file = open('myfile.txt', 'a')
my_file.write(' I also like JAVA')
my_file.close()
```

### Reading a file
```python
my_file = open('myfile.txt', 'r+')
text = my_file.read(10)
print(text)
```

## Working with JSON

### JSON to dictionary
```python
import json

userJSON = '{"first_name": "John","last_name": "Doe","Age": 30}'

user = json.loads(userJSON)

print(user)
print(type(user))
print(user['first_name'])
```

### dictionary to JSON
```python
car = {
    'make': 'Ford',
    'model': 'Mustang',
    'year': '1965'
}

carJSON = json.dumps(car)
print(carJSON)
```