tekst = "Anna, paweł, JulIA"
#[lista](){}
lista = tekst.split(", ")
print(tekst)
print(lista)
print(type(lista)) #list

imie1 = lista[0]
print(imie1) #Anna

imieDuze=imie1.upper()
print(imieDuze) #ANNA

imieMale=imie1.lower()
print(imieMale) #anna

#sprawdzanie zawartości
nazwisko=""
print(nazwisko.isalpha()) #False

print("\nPodaj swoje nazwisko: ",end="")
nazwisko=input()
zawartosc=nazwisko.isalpha()
print(zawartosc) #True or False

text1="\nJulia\n"
text2="Nowak"
print(text1 + text2)

text1=text1.rstrip()
print(text1 + text2)
print(text1 +" "+ text2)

#wyświetlenie łańcucha znaków
#wszystkie wersje Python'a
text="%s, Java i  %s" % ("PHP","Python")
print(text)

#nowsze wersje Python'a
text="{1}, Java i {0}".format("PHP","Python")
print(text)

#help(text.replace)

new = text.replace("PHP","C#")
print(new)

#wypisywanie danych
rok=2019
miesiac="kwiecień"
dzien=1

print("\nData:", end="")
print(dzien,miesiac,rok)
print("\nData:", end="")
print(dzien,miesiac,rok, sep="-")

print()
