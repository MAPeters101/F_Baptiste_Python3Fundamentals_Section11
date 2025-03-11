a = 1
b = 0
#result = a / b
#print(result)

ex = ValueError("Name must be at least 5 characters long.")
print(type(ex))
print(ex)
print(repr(ex))
print(str(ex))
print('-'*80)

#raise ex

name = input('Enter name (5 chars min): ')
if len(name) < 5:
    raise ValueError(f'{name} is not 5 characters or more...')

print(f'Hello {name}!')
print('-'*60)







