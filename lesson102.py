
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

l = [1,2,3,4,5]
while True:
    print(l.pop())
print('all done')
print('-'*80)



