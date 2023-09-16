
# some_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared_numbers = []
#
# for number in some_numbers:
#     if number % 2 ==0:
#         squared_numbers.append(number **2)
#
# print (squared_numbers)
#
# #acelasi rezultat cu list comprehension
#
# squared_numbers = [x **2 for x in some_numbers if x % 2 == 0]
# print(squared_numbers)
#
#
#
# # intrebare la interviuri
# d = {
#     'a': 1,
#     'b': 2
# }
# print(d['a']) #nu prea e pe python asta,
# print(d.get('a')) #varianta corecta de python, care returneaza NONE daca in lista nu e elementul printat
#
#
#
#
# with open ('hello.txt', 'r') as f:
#     content = f.read()
#     print(content)
#
# with open ('hello.txt', 'a') as f:
#     f.write('Some new content!')