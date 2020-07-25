Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> type(32)
<class 'int'>
>>> max('Hello world')
'w'
>>> min('Hello world')
' '
>>> len('Hello world')
11
>>> int('32')
32
>>> int('Hello')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int('Hello')
ValueError: invalid literal for int() with base 10: 'Hello'
>>> int(3.99999)
3
>>> int(-2.3)
-2
>>> float(32)
32.0
>>> float('3.14159')
3.14159
>>> str(32)
'32'
>>> str(3.14159)
'3.14159'
>>> import math
>>> print(math)
<module 'math' (built-in)>
>>> ratio = signal_power / noise_power
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    ratio = signal_power / noise_power
NameError: name 'signal_power' is not defined
>>> decibels = 10 * math.log10(ratio)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    decibels = 10 * math.log10(ratio)
NameError: name 'ratio' is not defined
>>> radians = 0.7
>>> height = math.sin(radians)
>>> degrees = 45
>>> radians = degrees / 360.0 * 2 * math.pi
>>> math.sin(radians)
0.7071067811865475
>>> math.sqrt(2) / 2.0
0.7071067811865476
>>> import random
>>> for i in range(10):
	x = random.random()
	print(x)
	0.11132867921152356
	0.5950949227890241
	0.04820265884996877
	0.997914947094958

	
0.7575182317262472
0.11132867921152356
0.5950949227890241
0.04820265884996877
0.997914947094958
0.9369389647100349
0.11132867921152356
0.5950949227890241
0.04820265884996877
0.997914947094958
0.5703012992186772
0.11132867921152356
0.5950949227890241
0.04820265884996877
0.997914947094958
0.9357318890697762
0.11132867921152356
0.5950949227890241
0.04820265884996877
0.997914947094958
0.3667074173289846
0.11132867921152356
0.5950949227890241
0.04820265884996877
0.997914947094958
0.5400800521800897
0.11132867921152356
0.5950949227890241
0.04820265884996877
0.997914947094958
0.520480732992739
0.11132867921152356
0.5950949227890241
0.04820265884996877
0.997914947094958
0.17130237897613598
0.11132867921152356
0.5950949227890241
0.04820265884996877
0.997914947094958
0.06670252923671127
0.11132867921152356
0.5950949227890241
0.04820265884996877
0.997914947094958
0.4300062927082918
0.11132867921152356
0.5950949227890241
0.04820265884996877
0.997914947094958
>>> random.randint(5, 10)
6
>>> random.randint(5, 10)
9
>>> random.randint(5, 10)
10
>>> t = [1, 2, 3]
>>> 
>>> random.choice(t)
2
>>> random.choice(t)
3
>>> random.choice(t)
3
>>> def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and I work all day.')

	
>>> print(print_lyrics)
<function print_lyrics at 0x02361BF8>
>>> print(type(print_lyrics))
<class 'function'>
>>> print_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
>>> def repeat_lyrics():
	print_lyrics()

	
>>> repeat_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
>>> def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print('I sleep all night and I work all day.')

	
>>> def repeat_lyrics():
	print_lyrics()
	print_lyrics()

	
>>> 
KeyboardInterrupt
>>> repeat_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
>>> def print_twice(bruce):
	print(bruce)
	print(bruce)

	
>>> print_twice('Spam')
Spam
Spam
>>> print_twice(17)
17
17
>>> import math
>>> print_twice(math.pi)
3.141592653589793
3.141592653589793
>>> print_twice('Spam '*4)
Spam Spam Spam Spam 
Spam Spam Spam Spam 
>>> print_twice(math.cos(math.pi))
-1.0
-1.0
>>> michael = 'Eric, the half a bee.'
>>> print_twice(michael)
Eric, the half a bee.
Eric, the half a bee.
>>> x = math.cos(radians)
>>> golden = (math.sqrt(5) + 1) / 2
>>> math.sqrt(5)
2.23606797749979
>>> math.sqrt(5)
2.23606797749979
>>> result = print_twice('Bing')
Bing
Bing
>>> print(result)
None
>>> print(type(None))
<class 'NoneType'>
>>> def addtwo(a, b):
	
KeyboardInterrupt
>>>  added = a + b
 
SyntaxError: unexpected indent
>>> def addtwo(a, b):
	added = a + b
	return added
x = addtwo(3, 5)
SyntaxError: invalid syntax
>>> print(x)
0.7071067811865476
>>> def fred():
	print("Zap")

	
>>> def jane():
	print("ABC")

	
>>> 
>>> Enter Hours: 45
SyntaxError: invalid syntax
>>>  Score   Grade
 
SyntaxError: unexpected indent
>>> 