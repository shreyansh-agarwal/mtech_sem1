import collections

dict1 = {'gupton': 'sharman', 'gupton': 'roy', 'gupton': 'kumar', 'gupton': 'ray', }
dict2 = {'ray': 'ray', 'ray': 'goldberg', 'ray': 'arun', 'ray': 'gupton'}
dict3 = {'sharman': 'gupton', 'sharman': 'panth', 'sharman': 'jaim'}
dict4 = {'kumar': 'gupton', 'kumar': 'panth'}
dict5 = {'panth': 'kumar', 'panth': 'sharman'}
dict6 = {'roy': 'gupton', 'roy': 'goldberg'}
dict7 = {'goldberg': 'roy', 'goldberg': 'ray'}
dict8 = {'arun': 'jaim', 'arun': 'ray'}
dict9 = {'goldi': 'NULL'}
dict10 = {'jaim':'sharman', 'jaim': 'arun'}

I_D0 = {'roy', 'jaim'}

res = collections.ChainMap(dict1, dict2)

# Creating a single dictionary
print(res.maps, '\n')

print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()

# Print all the elements from the result
print('elements:')
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()

# Find a specific value in the result
print('day3 in res: {}'.format(('day1' in res)))
print('day4 in res: {}'.format(('day4' in res)))

