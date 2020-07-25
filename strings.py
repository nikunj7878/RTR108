Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
>>> letter = fruit[0]
>>> print(letter)
b
>>> letter = fruit[1.5]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    letter = fruit[1.5]
TypeError: string indices must be integers
>>> fruit = 'banana'
>>> len(fruit)
6
>>> length = len(fruit)
>>> last = fruit[length-1]
>>> print(last)
a
>>> index = 0
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
b
a
n
a
n
a
>>> for char in fruit:
	print(char)
	s = 'Monty Python'
	print(s[0:5])

	
b
Monty
a
Monty
n
Monty
a
Monty
n
Monty
a
Monty
>>> print(s[6:12])
Python
>>> fruit = 'banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
>>> fruit = 'banana'
>>> fruit[3:3]
''
>>> greeting = 'Hello, world!'
>>> greeting[0] = 'J'
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    greeting[0] = 'J'
TypeError: 'str' object does not support item assignment
>>> greeting = 'Hello, world!'
>>> new_greeting = 'J' + greeting[1:]
>>> print(new_greeting)
Jello, world!
>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
	count = count + 1
	
SyntaxError: expected an indented block
>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False
>>> if word == 'banana':
	print('All right, bananas.')

	
All right, bananas.
>>> if word < 'banana':
	print('Your word,' + word + ', comes before banana.')

	
>>> elif word > 'banana':
	
SyntaxError: invalid syntax
>>> stuff = 'Hello world'
>>> type(stuff)
<class 'str'>
>>> dir(stuff)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str.capitalize)
Help on method_descriptor:

capitalize(self, /)
    Return a capitalized version of the string.
    
    More specifically, make the first character have upper case and the rest lower
    case.

>>> word = 'banana'
>>> new_word = word.upper()
>>> print(new_word)
BANANA
>>> word = 'banana'
>>> index = word.find('a')
>>> print(index)
1
>>> word.find('na')
2
>>> word.find('na', 3)
4
>>> line = '  Here we go  '
>>> line.strip()
'Here we go'
>>> line = 'Have a nice day'
>>> line = 'Have a nice day'
>>> line.startswith('Have')
True
>>> line.startswith('h')
False
>>> data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
>>> atpos = data.find('@')
>>> print(atpos)
21
>>> sppos = data.find(' ',atpos)
>>> print(sppos)
31
>>> host = data[atpos+1:sppos]
>>> print(host)
uct.ac.za
>>> camels = 42
>>> '%d' % camels
'42'
>>> camels = 42
>>> 'I have spotted %d camels.' % camels
'I have spotted 42 camels.'
>>> 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
'In 3 years I have spotted 0.1 camels.'
>>> '%d %d %d' % (1, 2)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    '%d %d %d' % (1, 2)
TypeError: not enough arguments for format string
>>> while True:
	line = input('> ')
	if line[0] == '#':
		continue
	if line == 'done':
		break
	print(line)

	
> hello there
hello there
>  # don't print this
 # don't print this
> print this!
print this!
> 