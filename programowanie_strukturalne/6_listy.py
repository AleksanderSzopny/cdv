programowanie = ['Python','C#','JS','PHP','Java']

print(programowanie)
print(type(programowanie))

pierwszy=programowanie[0]
print('Pierwszy język programowania:',pierwszy)

trzyElementy=programowanie[0:3]
print(trzyElementy)

ostatni=programowanie[-1]
print('Ostatni język programowania:',ostatni)

#Dodanie nowego elementu do listy
programowanie.append('R')
programowanie.append('Python')
print(programowanie)

#Zliczanie elementów w liście
ile=programowanie.count('Python')
print(f'Python występuje {ile} razy')

#Ilość elementów w naszej liście
iloscElem=len(programowanie)
print('Ilość elementów w liście: ',end='')
print(iloscElem)

#Łączenie list
print(f'\n\n{programowanie}')
inneJezyki=['C','C++']
print('Połączenie list')
programowanie.extend(inneJezyki)
print(programowanie)

#Wyczyszczenie listy
nowa=programowanie
print(f'Nowa lista: {nowa}')
# nowa.clear()
programowanie.clear()
print(f'Nowa lista po wyczyszczeniu: {nowa}')
print(f'Lista programowanie po wyczyszczeniu: {programowanie}')
