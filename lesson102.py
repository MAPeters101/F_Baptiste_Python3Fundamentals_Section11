
try:
    1 / 0
except ZeroDivisionError as ex:
    print(f'Exception occurred: {type(ex)}, {ex}')

print('Code continues running here...')
print('-'*80)

l = [1,2,3,4,5]
while len(l) > 0:
    print(l.pop())
print('all done')
print('-'*80)

# l = [1,2,3,4,5]
# while True:
#     print(l.pop())
# print('all done')
# print('-'*80)

l = [1,2,3,4,5]
try:
    while True:
        print(l.pop())
except IndexError:
    # index error means list is now empty - expected behavior
    print('All done - all elements have been popped.')
print('code resumes here..')
print('-'*80)


l = [1,2,3,4,5]
try:
    while True:
        print(l.pop())
except Exception:
    # what happened? IndexError? something else?
    print('something unexpected happened.')
print('code resumes here..')
print('-'*80)

l = (1,2,3,4,5)
try:
    while True:
        print(l.pop())
except Exception:
    # what happened? IndexError? something else?
    print('All done - all elements have been popped.')
print('code resumes here..')
print('-'*80)

# l = (1,2,3,4,5)
# try:
#     while True:
#         print(l.pop())
# except IndexError:
#     # index error means list is now empty - expected behavior
#     print('All done - all elements have been popped.')
# print('code resumes here..')
# print('-'*80)

#10 + 'abc'
#10 + None
data = [10, 20, 10, 10, 5, 10]
sum_data = 0
count_data = 0
for element in data:
    sum_data += element
    count_data += 1
average = sum_data / count_data
print(average)
print()

# data = []
# sum_data = 0
# count_data = 0
# for element in data:
#     sum_data += element
#     count_data += 1
# average = sum_data / count_data
# print(average)
# print()

data = []
if len(data) == 0:
    average = 0
else:
    sum_data = 0
    count_data = 0
    for element in data:
        sum_data += element
        count_data += 1
    average = sum_data / count_data
print(average)
print()

data = [10, 20, 'abc']
sum_data = 0
count_data = 0
try:
    for element in data:
        sum_data += element
        count_data += 1
    average = sum_data / count_data
except ZeroDivisionError:
    average = 0
except TypeError:
    average = 0

print(f'average = {average}')
print()


data = [10, 20, 'abc']
sum_data = 0
count_data = 0
try:
    for element in data:
        try:
            sum_data += element
            count_data += 1
        except TypeError:
            # skip
            pass
    average = sum_data / count_data
except ZeroDivisionError:
    average = 0
except TypeError:
    average = 0

print(f'average = {average}')
print('='*80)

try:
    1 / 0
except Exception as ex:
    print(f'logging error: {ex}')

print('program still running...')
print()

# try:
#     1 / 0
# except Exception as ex:
#     print(f'logging error: {ex}')
#     raise
#
# print('program still running...')
# print()

try:
    raise ValueError('custom message')
except ValueError as ex:
    print(f'handled a ValueError: {ex}')
finally:
    print('this is always executed')
print('all done')
print()

# try:
#     raise TypeError('custom message')
# except ValueError as ex:
#     print(f'handled a ValueError: {ex}')
# finally:
#     print('this is always executed')
# print('all done')
# print()

# try:
#     raise ValueError('custom message')
# except ValueError as ex:
#     print(f'handled a ValueError: {ex}')
#     raise TypeError('changing to a type error.')
# finally:
#     print('this is always executed')
# print('all done')
# print()

try:
    print('Nothing to see here...')
except ValueError:
    print('handled a ValueError.')
finally:
    print('this always executes')
print()



