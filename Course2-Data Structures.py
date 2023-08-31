print("Data structure")
#
# my_list = list()
# my_second_list = []
#
# print(my_list, my_second_list)
#
# my_list = [4+5j, 'Ana are mere', 23.76, True, None]
# print(my_list)
# print(len(my_list))
# print('Index 4:', my_list[4])
# print('Index 2:', my_list[2])
# print('Index 0:', my_list[0])
# print('Index 4:', my_list[-3])


# my_list = ['Ana', 'are', 'mere', 'si', 'e', 'happy']
# print(my_list)
# print(len(my_list))
# my_sliced_list = my_list[4:]
# print(my_sliced_list)

# my_list = ['Ana', 'are', 'mere', 'si', 'e', 'happy']
# my_sorted_list = sorted(my_list) #sorted -
# print(my_sorted_list)
# # print(my_list.sort()) #.sort - sorteaza lista in place. modifica ordinea elementelor
# print(my_list)
#
# #final_list = [] #linia asta nu e musai de pus. in practica nu se foloseste
# my_second_list = [1, 2, 3, 'si']
# final_list = list(my_second_list + my_list)
# print(final_list)

#TUPLURI
# my_list = [1,2,3,4,5]
# my_tuple = (1,2,3,4,5)
# print(my_list)
# print(my_tuple)
# print(my_list, my_list.__sizeof__())
# print(my_tuple, my_tuple.__sizeof__()) #marimea e mai mica decat la liste

#DICTIONARE
# my_dictionary = dict()
# my_dictionary = {}
# my_dictionary = {
#     'key_1': 12,
#     'key_2': 4+5j,
#     3: True,
#     4: None,
#     5+2j: '',
#     ("key_6", 7): [1,2,3],
#     -8: ('First', 'Second', 'Third')
# }
# person = {
#     'first_name': 'Ion',
#     'second_name': 'Popescu',
#     'age': 23,
#     'preferences': {
#         1: 'Fotbal',
#         2: 'Tenis',
#         3: 'Baschet'
#       }
#    }
#
# print(person['first_name'])
# print(person['age'])
# print(person.get('email', 'Cheia \'email\' nu a fost gasita!'))   #apelezi metoda "get"
#
# for value in person.values():
#     print(value)
# for k, v in person.items():
#     print (f'{k}:{v}')
# for p in person.get('preferences'). values():
#     print (p)

# list_1 = [1, 2, 3 ]
# list_2 = list_1 #pointeaza catre aceeasi adresa de memorie cu list_1 / list 2 are acceeasi adresa (memorie) ca list_1
#
# list_1.append(99)
# print(list_2)

person1 = {
    'first_name': 'Ion',
    'second_name': 'Popescu',
    'age': 23,
    'preferences': {
        1: 'Fotbal',
        2: 'Tenis',
        3: 'Baschet'
        }
}
person2 = person1
person2['first_name'] = 'Vasile'
print('person1:', person1)
print('person2: ', person2)

#SETURI
unique_ids = []
my_list = [1, 2, 3, 5, 7, 8, 9, 13, 15, 3, 5, 7]
for el in my_list:
    if el not in unique_ids:
        unique_ids.append(el)
print(my_list)
print(unique_ids)

unique_set_ids = set(my_list)
print(unique_set_ids)

s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 5, 7}
s3 = {1, 2}

print(s1.intersection(s2))
print(s3.issubset(s1))