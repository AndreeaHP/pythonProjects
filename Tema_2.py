'''1. Sa se verifice daca textul introdus de la tastatura de catre un utilizator este un sir de
caractere de tip string sau un sir de numere. Utilizati instructiunea de tip if-elif-else.
In cazul in care valoarea este un sir de caractere, afisati pe ecran mesajul “Sirul de
caractere a fost gasit de Mihai”, unde Mihai reprezinta numele vostru
preluat automat de la tastatura.
'''
# text_introdus = input('Introdu textul aici: ')
# nume = input('Introdu numele tau: ') #cum scriu aici ca input-ul sa fie identificat
#                                       ca fiind de tipuri diferite (str, int, alt tip)
# if (type(text_introdus)) is str:
#     print('Sirul de caractere ' + text_introdus + ' a fost gasit de ' + nume)
# elif (type(text_introdus)) is int:
#     print('Sirul de caractere este un sir de numere')
# else:
#     print('Sirul de caractere este de un alt tip')


'''2. Creati un program in care utilizatorul sa introduca un numar. Validati daca acest
numar este par sau impar si afisati un raspuns in acest sens.
'''
# def even_or_odd (number):
#     if number % 2 == 0:
#         return f"{number} is an even number"
#     return f"{number} is odd"
#
# nr = input ('please enter a number: ')
# if nr.isdigit():
#     print(even_or_odd(int(nr)))
# else:
#     print('you did not entered a number')

# numar_introdus = int(input('Numarul introdus = '))
# if numar_introdus % 2 == 0:
#     print('Numarul introdus este un numar par')
# else:
#     print('Numarul introdus este un numar inpar')

'''
3. Creati un program in care utilizatorul sa introduca un an. Calculati daca anul este
bisect sau nu si afisati un raspuns in acest sens. OBS. Un an bisect se imparte exact
la 4 (fara rest)'''
# an_introdus = int(input('Anul introdus = '))
# if an_introdus % 4 == 0:
#     print('Anul introdus este un an bisect')
# else:
#     print('Anul introdus nu este un an bisect')

'''
4. Creati un program in care utilizatorul sa introduca un numar. Calculati daca numarul
este pozitiv, zero sau negativ. In cazul in care este pozitiv validati daca este mai mic
decat 10 si afisati un mesaj de confirmare.  Daca numarul este zero afisati “Numarul
este 0”, iar daca numarul este negativ atunci transformati numarul in numar pozitiv si
afisati numarul pozitiv.'''

# numar_introdus = int(input('Numarul introdus = '))
# if numar_introdus > 0 and numar_introdus < 10:
#     print('Numarul introdus este pozitiv mai mare ca 0, dar mai mic ca 10')
# elif numar_introdus == 0:
#     print('Numarul este 0')
# elif numar_introdus < 0:
#     print(abs(numar_introdus))
# else:
#     print('Numarul este pozitiv mai mare sau egal cu 10')

'''
5. Creati un program care are ca scop un meniu. Meniul se va selecta prin introducerea
de la tastaura a unui numar intre 1 si 5 captat intr-o variabila. Prezentati prin afisare
acest sir de caractere:
“”” 1 – Afisare lista de cumparaturi
2 – Adaugare element
3 – Stergere element
4 – Sterere lista de cumparaturi
5 - Cautare in lista de cumparaturi “””
Apoi folosindu-va de o constructie if-elif-else afisati: - daca utilizatorul scrie de la
tastaura 1 afisati “Afisare lista de cumparaturi” - daca utilizatorul scrie de la tastaura 2
afisati “Adugare element” - daca utilizatorul scrie de la tastaura 3 afisati “Stergere
element” - daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturit”
- daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element” - daca utilizatorul
scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”'''

# option = input()
# print(option)
#
# shopping_list = ['ardei', 'cartofi', 'morcovi']
#
# def print_list(*args):
#     print(shopping_list)
#
# def search_in_list (keyword):
#         print(keyword in shopping_list)
#
# def print_not_existent_option(*args):
#     print('Aceasta optiune nu exista')
#
# keyword = 'mere'
#
# option_dict = {
#     '1': (print_list, None),
#     '2': (search_in_list, keyword)
#
# }
#
# func, arg = option_dict.get(option, (print_not_existent_option, None))
# func(arg)



# numar_introdus = int(input('Numarul introdus = '))
# if numar_introdus == 1:
#     print('Afisare lista de cumparaturi')
# elif numar_introdus == 2:
#     print('Adaugare element')
# elif numar_introdus == 3:
#     print('Stergere element')
# elif numar_introdus == 4:
#     print('Sterere lista de cumparaturi')
# elif numar_introdus == 5:
#     print('Cautare in lista de cumparaturi')
# else:
#     print('Alegerea nu exista. Reincercati!')

'''6. Avand doua liste, afisati o lista a elementelor comune ambelor liste
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Rezultat
[1,2,3,5,8,13]'''

# lista_a = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
# lista_b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
# lista_elem_comune = lista_a.intersection(lista_b)
# print(lista_elem_comune)

'''7.[ { 
   'nume': 'George',
   'filme': ['Shrek', 'Bond', 'Fight Club']
 },
{
 'nume' : 'Cristian',
 'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']
},

{
 'nume' : 'Stefan',
 'filme': ['Fight Club', 'Slumdog Milionare']
}

]

Avand o lista de utilizatori si filme vizionate, listati:
Cel mai vizionat film - Fight Club in cazul de mai sus
Utilizatorul cu cele mai multe filme vizionate - Cristian in cazul de mai sus
Extra
Top filme dupa vizionari: Fight Club, Bond, Dracula, Shrek, The nun ...
Top utilizatori cu cele mai multe filme vizionate - Cristian, George, Stefan'''

person_1 = {
    'nume': 'George',
    'filme': ['Shrek', 'Bond', 'Fight Club']
}

person_2 = {
    'nume' : 'Cristian',
    'filme': ['Fight Club', 'The Nun', 'Dracula', 'Bond']
}
person_3 = {
    'nume' : 'Stefan',
    'filme': ['Fight Club', 'Slumdog Milionare']
}

movie_count = {}
for person_data in data['filme']:
    if movie in movie_count:
        movie_count += 1
    else:
        movie_count
 #dictionaries  - de continuat



# tema din curs
# my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6 ]
#
# #lista ordonata ascendent
# my_list.sort()
# print(my_list)
# #lista numere pare - lista ordonata ascendent
# my_sliced_list = my_list[1::2]
# print(my_sliced_list)
# #lista numere impare - lista ordonata ascendent
# my_sliced_list = my_list[::2]
# print(my_sliced_list)
# #lista numere multiplu de 3 - lista ordonata ascendent
# my_sliced_list = my_list[2::3]
# print(my_sliced_list)
#
# #lista ordonata descendent
# my_list.sort(reverse=True)
# print(my_list)
# #lista numere pare- lista ordonata descendent
# my_sliced_list = my_list[::2]
# print(my_sliced_list)
# #lista numere impare- lista ordonata descendent
# my_sliced_list = my_list[1::2]
# print(my_sliced_list)
# #lista numere multiplu de 3 - lista ordonata descendent
# my_sliced_list = my_list[1::3]
# print(my_sliced_list)




