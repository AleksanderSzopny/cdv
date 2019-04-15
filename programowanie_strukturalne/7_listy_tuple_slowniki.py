#listy

programowanie=['PHP','Python','Java']
print(type(programowanie))
programowanie.append('C#')
programowanie.append('PHP')
print(programowanie)
ile=programowanie.count('PHP')
print(f'Ile razy jest PHP: {ile}')

#tuple
imiona=('Julia','Anna','Tomek')
print(imiona)
print(type(imiona))
# imiona.append('Janusz') nie można modyfkować w ten sposób
pierwszy=imiona[0]
print(pierwszy)

#słowiki (w innych jęzkach tablica asocjacyjna)
osoba={
    'imie':'Julia',
    'nazwisko':'Kowalska',
    'wiek':23
}
print(osoba)
print(type(osoba))
print(osoba['imie'])
print(osoba.keys())
print(osoba.get('wzrost','brak danych'))

################################################
'''
Utwórz słownik i przypisz mu trzy imiona podane z klawiatury.Wyświetl te dane na ekranie w formacie
Imie1:...
Imie2:...
Imie3:...
'''

imiona={
    'Imie1':input('Podaj pierwsze imię '),
    'Imie2':input('Podaj drugie imię '),
    'Imie3':input('Podaj trzecie imię ')
}
print(f'Podane imiona{imiona}.')
