#zmienne globalne i lokalne


#precyzja
x="{0:.3f}".format(5) #3 miejsca po przecinku
print(x) #5.000

#Napisz funkcję która jako argument przyjmuje wartość złotych i zamienia dane po kursie dzisiejszym franka
#Wyświetl użytkownikowi ile franków kupi za podaną kwotę

def plnToChf(value):
    kursChf=3.8184
    iloscChf=value // kursChf
    print(f'Ilość CHF:{iloscChf}')

plnToChf(500)

#zmienna globalna

zmiennaGlobal=10
print(f'Wartość zmiennej globalnej: {zmiennaGlobal}')
print(f'Id zmiennej globalnej: {id(zmiennaGlobal)}')

def spr():
    global zmiennaGlobal
    zmiennaGlobal=20
    print(f'\nWartość zmiennej globalnej wewnątrz funkcji: {zmiennaGlobal}')
    print(f'\nID zmiennej globalnej wewnątrz funkcji: {id(zmiennaGlobal)}')
spr()

print(f'\nWartość zmiennej globalnej po wywołaniu funkcji: {zmiennaGlobal}')
print(f'\nID zmiennej globalnej po wywołaniu funkcji: {id(zmiennaGlobal)}')
