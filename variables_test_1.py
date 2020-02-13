Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5 == 5
True
>>> 5 == 6
False
>>> 5==5
True
>>> 5=5
SyntaxError: can't assign to literal
>>> 5==6
False
>>> x != y
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x != y
NameError: name 'x' is not defined
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined
>>> (true)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    (true)
NameError: name 'true' is not defined
>>> <class 'bool'>
SyntaxError: invalid syntax
>>> x > y
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x > y
NameError: name 'x' is not defined
>>> x = 5
>>> if x < 10
SyntaxError: invalid syntax
>>> print('smaller')
smaller
>>> print('bigger')
bigger
>>> print('x < 10')
x < 10
>>> if x < 10
SyntaxError: invalid syntax
>>> 17 and true
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    17 and true
NameError: name 'true' is not defined
>>> print(tue)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(tue)
NameError: name 'tue' is not defined
>>> print(true)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(true)
NameError: name 'true' is not defined
>>> print('true')
true
>>> print('x > 0')
x > 0
>>> print('x is positive')
x is positive
>>> x = 3
>>> x
3
>>> x < 10
True
>>> if x <  10
SyntaxError: invalid syntax
>>> if x < 10:
	print('small')

	
small
>>> x = 3
>>> if x < 10
SyntaxError: invalid syntax
>>> if x < 10:
	print('small')
	print('done')
	file"<stdin>",line 3
	
SyntaxError: invalid syntax
>>> if x%2 ==0 :
	print('x is even')
	else :
		
SyntaxError: invalid syntax
>>> print('x is odd')
x is odd
>>> if x%2 == 0 :
	print('x is even')
	print('x is odd')

	
>>> if x < y :
	print('x is less than y')
        elif x > y:
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> if 6<5
SyntaxError: invalid syntax
>>> if 6 < 5 :
	print('6 is greater than 5')
	print('6 and 5 are equal')

	
>>> x = 4
>>> if x > 2
SyntaxError: invalid syntax
>>> x = 4
>>> if x > 2 :
	print('bigger')
	else :
		
SyntaxError: invalid syntax
>>> x = 4
>>> if x > 2:
	print('bigger')
	print('all done')

	
bigger
all done
>>> if x < 2 :
	print('small')
	elif x < 10 :
		
SyntaxError: invalid syntax
>>> x = 0
>>> if x < 2:
	print('small')

	
small
>>> x = 0
>>> elif x < 10 :
	
SyntaxError: invalid syntax
>>> x=2
>>> 5=5
SyntaxError: can't assign to literal
>>> 5==5
True
>>> if 0 < x:
	x

	
2
>>> if 0 < x and x < 10 :


x
SyntaxError: expected an indented block
>>> x
2
>>> if 0 < x and x < 10 :
	x

	
2
>>> x = 5
>>> if x < 2:
	print('small')
	x

	
>>> x
5
>>> x < 10 :
	
SyntaxError: invalid syntax
>>> x
5
>>> 
