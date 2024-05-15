immutable_var = (1, 'world', 1.34, True, [1, 2])
print('Immutable tuple: ', immutable_var)
immutable_var[4][0] = 3
print(immutable_var) # кортеж является неизменяемой последованностью данных, но если внутри кортежа есть список, то его можно изменить
mutable_list = [1, 3, 'onion', 'potato']
print(mutable_list)
mutable_list[2] = 'garlic'
print('Mutablelist: ', mutable_list)
mutable_list.append(6)
print(mutable_list)