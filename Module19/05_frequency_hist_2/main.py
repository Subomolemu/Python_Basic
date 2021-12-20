string = 'Здесь что-то написано'
string = list(string)
print(string)
string_dict = {}
inversion_dict = {}
for sym in string:
    string_dict[sym] = string.count(sym)

print('\nОригинальный словарь частот: ')
for key, value in sorted(string_dict.items()):
    print(f'{key} : {value}')
    if value not in inversion_dict.keys():
        inversion_dict[value] = list(key)
    else:
        inversion_dict[value].append(key)

print('\nИнвертированный словарь частот:')
for key, value in inversion_dict.items():
    print(f'{key} : {value}')
