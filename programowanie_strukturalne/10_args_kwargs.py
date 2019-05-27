def wyswietl(num1,num2):
    print(f'Liczba 1:{num1}')
    print(f'Liczba 2:{num2}')
wyswietl(2,4)

############### *args #############

def wyswietlArgs(num1, *args):
    print(f'\nPierwszy element: {num1}')
    for i in args:
        print(f'Następny element: {i}')

wyswietlArgs(2,33,21,100)


############# *kwargs ############

import os
os.system('cls') #CZYSZCZENIE EKRANU

def pracownik(**kwargs):
    #print(kwargs)
    for key, val in kwargs.items():
        print(f'Klucz:{key}, wartość: {val}')
pracownik1={
    'fName': 'Janusz',
    'lName': 'Nowak',
    'age': 23,
    'city': 'Poznań',
    'job': True
}
pracownik(**pracownik1)
