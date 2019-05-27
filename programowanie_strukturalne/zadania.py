#ZADANIE 1
a=int(input('Podaj liczbę pierwszą: '))
b=int(input('Podaj liczbę drugą: '))

def licz(a,b):
    try:
        result=(((a*a)+b)/((a*a)+(2*a*b)+(b*b)))
        print(f'Wynik: {result}')
    except ZeroDivisionError:
        print(f'Błąd, dzielisz przez zero')
licz(a,b)

#ZADANIE 2
#a2+b dla c>0
#a-b2 dla c<0
# 1/a-b dla c=0
c=int(input('Podaj wartość liczby c: '))
a=int(input('Podaj liczbę pierwszą: '))
b=int(input('Podaj liczbę drugą: '))
def licz(a,b):
    try:
        if c > 0:
            result=((a*a)+b)
            print(f'Wynik: {result}')
        if c<0
            result=(a-(b*b))
            print(f'Wynik: {result}')
        if c==0
            result=(1/a-b)
            print(f'Wynik: {result}')
    except ZeroDivisionError:
        print(f'Błąd, dzielisz przez zero')
licz(a,b)
#BŁĄD
