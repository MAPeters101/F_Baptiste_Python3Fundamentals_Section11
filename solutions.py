'''
Question 1
The following code is meant to calculate the smallest absolute value of a given sequence of numbers.

values = [1, 2, 3, 4]

minimum = abs(values[0])
for value in values[1:]:
    if abs(value) < minimum:
        minimum = abs(value)
print(f'Minimum is: {minimum}')
Minimum is: 1
The problem is that if the sequence is empty, it will raise an exception.

Write code such that if the values sequence is empty, the calculated minimum is printed as 0.

Solution
Let's try running this code with an empty list and see what exception we get:

values = []

minimum = abs(values[0])
for value in values[1:]:
    if abs(value) < minimum:
        minimum = abs(value)
print(f'Minimum is: {minimum}')
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-2-6750d95142f0> in <module>
      1 values = []
      2
----> 3 minimum = abs(values[0])
      4 for value in values[1:]:
      5     if abs(value) < minimum:

IndexError: list index out of range
As you can see the problem lies in trying to retrieve the first element of an empty sequence.

We could take a LBYL approach, and test for the length of the sequence:

values = []

if len(values) == 0:
    print(f'Minimum is: 0')
else:
    minimum = abs(values[0])
    for value in values[1:]:
        if abs(value) < minimum:
            minimum = abs(value)
    print(f'Minimum is: {minimum}')
Minimum is: 0
values = [3, -2, 5]

if len(values) == 0:
    print(f'Minimum is: 0')
else:
    minimum = abs(values[0])
    for value in values[1:]:
        if abs(value) < minimum:
            minimum = abs(value)
    print(f'Minimum is: {minimum}')
Minimum is: 2
But we can also take a EAFP approach, using exception handling:

values = []

try:
    minimum = abs(values[0])
    for value in values[1:]:
        if abs(value) < minimum:
            minimum = abs(value)
    print(f'Minimum is: {minimum}')
except IndexError:
    print('Minimum is: 0')
Minimum is: 0
I don't like have two separate print statements - mainly because I need to be careful about keeping the format of the string the same in both cases. So, I would rewrite this code like this:

values = []

try:
    minimum = abs(values[0])
    for value in values[1:]:
        if abs(value) < minimum:
            minimum = abs(value)
except IndexError:
    minimum = 0

print(f'Minimum is: {minimum}')
Minimum is: 0
values = [2, -3, 4, -1]

try:
    minimum = abs(values[0])
    for value in values[1:]:
        if abs(value) < minimum:
            minimum = abs(value)
except IndexError:
    minimum = 0

print(f'Minimum is: {minimum}')
Minimum is: 1
Question 2
Write code that raises the built-in Python exception ValueError with a custom message, and catches the exception and prints the custom message.

Solution
To raise an exception we'll use a raise statement, and then we'll catch the ValueError using a try...except....

Let's write the code to raise the exception first:

raise ValueError('Some custom message')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-8-ce8042d1b9d6> in <module>
----> 1 raise ValueError('Some custom message')

ValueError: Some custom message
Finally, we'll put this in a try catch statement:

try:
    raise ValueError('Some custom message')
except ValueError as ex:
    print(ex)
Some custom message
'''