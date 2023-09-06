import random

# counter = 0
# name = 'Ion'
# while counter < 10:
#     #counter = counter + 1
#     counter += 1
#     print(f'Hello World!',(counter), (name))


# for i in range (3):
#     print(f'Instruction [{i+1}]')
#
# shopping_list = ['mere', 'pere', 'gogonele']
# for el in shopping_list:
#     print(el)


# BREAK
# while True:
#     random_choice = random.choice([0, 1, 2, 3, 4, 5, 9, 10])
#     if random_choice % 3 == 0:
#         break
#     print(f'Selected choice: {random_choice}')
# print(f'Selected choice which is % 3: {random_choice}')

#CONTINUE
# for i in range (10):
#     if i % 2 != 0: #diferit de 0
#         #print(f'Numar impar:{i}')
#         continue
#     print(f'Numar par: {i}')

#PASS
# if True:
#     print('Evrika!')
#     pass

#FUNCTII
# def my_function(*args, **kwargs):
#     pass

# def my_func():
#     print('Hello!')
#     return
#
# result = my_func() #returneaza "Hello!"
# print(f'result from function is {result}')


# def get_sum(a,b):
#     return a + b
#
# print(get_sum(1, 2))


my_sum = 0
# def get_sum(a, b):
#     global my_sum         #variabila globala
#     my_sum = a + b
#     return my_sum
#
# print(get_sum(1, 2))
# print (my_sum)

# def get_sum(a, b, my_sum):
#     my_sum = a + b
#     return my_sum
#
# print(get_sum(1, 2, my_sum))
# print (my_sum)

# def my_function(list_param):
#     inner.list_param = list(list_param) #va printa [1, 2, 3] pentru ca desi e acelasi nume, este o alta variabila, motiv pt care dam denumiri diferite
#     inner.list_param.append(4)
#
#     return inner.list_param
#
# list_param = [1, 2, 3]
# modified_list = my_function(list_param)
# print(list_param)
# print(modified_list)

#funtii pozitionatele sau #cheie-valoare
# def print_info (nume, prenume, varsta=18, greutate=55):
    # print(f'Te numesti {prenume} {nume} si ai {varsta} ani. Cantaresti {greutate} kg.')
# print_info('Ion', 'Popescu', varsta=18, greutate=50)

def print_info (nume, prenume, *args, varsta=18, greutate=55, **kwargs):
    for arg in args:
        print(arg)


# print_info('Ion', 'Popescu', varsta=18, greutate=50)
print_info('Ion', 'Popescu', varsta=22, greutate=60, ocupatia='Student', strada='Napoca', nr='10')