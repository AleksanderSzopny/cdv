##################ZADANIE 3########################
a=int(input('Podaj liczbę pierwszą: '))
b=int(input('Podaj liczbę drugą: '))

def nwd(a,b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a
nwd(a,b)
print(f'Największy wspólny dzielnik liczb {a,b} wynosi {nwd(a,b)}')

##################ZADANIE 4##########################
#nie skończone
a=int(input('Podaj liczbe: '))

def srd(a):
    b=0
    while a>0:
        b=b+a%10
        a/=10
    return b
srd(a)
print(f'Suma cyfr rozwinięcia dziesiętnego wynosi: {srd(a)}')

###################ZADANIE 5#########################
#nie skończone
a=int(input('Podaj liczbę: '))


print(f'Liczba {a} jest liczbą pierwszą')

#################ZADANIE 6##########################
#nie skończone
a=int(input('Podaj wysokość choinki: '))
for j in range(a, 6):
    print(j * "#")
