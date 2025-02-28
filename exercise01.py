'''
Question 1
The following code is meant to calculate the smallest absolute value of a
given sequence of numbers.

values = [1, 2, 3, 4]

minimum = abs(values[0])
for value in values[1:]:
    if abs(value) < minimum:
        minimum = abs(value)
print(f'Minimum is: {minimum}')
Minimum is: 1
The problem is that if the sequence is empty, it will raise an exception.

Write code such that if the values sequence is empty, the calculated minimum
is printed as 0.
'''