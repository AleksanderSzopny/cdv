def witaj():
    print('Witaj!',end=' ')
    print('Witaj Janusz!')

witaj()

def wyswietlWiek(wiek):
    print(f'Twój wiek: {wiek}')

wyswietlWiek(23)

def iloczyn(a,b):
    return a*b
print('Iloczyn wynosi: ',iloczyn(3,4))

def iloraz(a,b):
    return a/b
x=iloraz(4,5)
print(f'Iloraz wynosi: {x}')
print(type(x))

print(iloraz(b=10,a=3))

'''
Użytkownik podaje z klawiatury:
marka,model,pojemnosc,predkoscMax
utwórz funkcję, która pobierze dane od użytkownika i przypisze do słownika
utwórz drugą funkcję wyświetlającą dane w formacie
Marka:...
Model:...
Pojemnosc:...
Predkosc maksymalna:...
'''
marka=input('Podaj markę pojazdu: ')
model=input('Podaj model pojazdu: ')
pojemnosc=input('Podaj pojemnosc pojazdu: ')
predkoscMax=input('Podaj prędkość maksymalną pojazdu: ')

auto={
    'Marka':marka,
    'Model':model,
    'Pojemnosc':pojemnosc,
    'Prędkość maksymalna':predkoscMax
}
print(auto)
