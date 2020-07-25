Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = x + 1
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    x = x + 1
NameError: name 'x' is not defined
>>> x = 0
>>> x = x + 1
>>> n = 5
>>> whilen>0:
	
SyntaxError: invalid syntax
>>> while n > 0:
	print(n)
	n = n-1

	
5
4
3
2
1
>>> while True:
	line = input('> ')
	if line == 'done':
		break
	print(line)

	
> hello there
hello there
> finished
finished
> done
>>> while True:
	line = input('> ')
	if line[0] == '#':
		contiue
		continue
	ifline == 'done':
		
SyntaxError: invalid syntax
>>> while True:
	line = input('> ')
	if line[0] == '#':
		continue
	if line == 'done':
		break
	print(line)

	
> hello there
hello there
> # don't print this
>  print this!
 print this!
> done
>>> friends = ['Joseph', 'Glenn', 'Sally']
>>> for friend in friends:
	 print('Happy New Year:', friend)
	 print('Done!')

	 
Happy New Year: Joseph
Done!
Happy New Year: Glenn
Done!
Happy New Year: Sally
Done!
>>> count = 0
>>> for itervar in [3, 41, 12, 9, 74, 15]:
	count = count + 1

>>> total = 0
>>> for itervar in [3, 41, 12, 9, 74, 15]:
	total = total + itervar
print('Total: ', total)
SyntaxError: invalid syntax
>>> largest = None
>>> print('Before:', largest)
Before: None
>>> for itervar in [3, 41, 12, 9, 74, 15]:
	if largest is None or itervar > largest :
		largest = itervar
	print('Loop:', itervar, largest)
print('Largest:', largest)
SyntaxError: invalid syntax
>>> Before: None
>>> Loop: 3 3
SyntaxError: invalid syntax
>>> Loop: 41
>>> Loop: 12 41
SyntaxError: invalid syntax
>>> smallest = None
>>> print('Before:', smallest)
Before: None
>>> for itervar in [3, 41, 12, 9, 74, 15]:
	if smallest is None or itervar < smallest:
		smallest = itervar
	print('Loop:', itervar, smallest)

	
Loop: 3 3
Loop: 41 3
Loop: 12 3
Loop: 9 3
Loop: 74 3
Loop: 15 3
>>> 