#przerobić na -funkcje pod flask
import random
import sys

def check(lista, haslo):
    for elem in lista:
        if elem.lower() == haslo.lower():
            return True
    return False

def fiszki(polskie, francuskie):
    print("Hasła po polsku czy po francusku: polskie/francuskie ")
    jezyk = input("Wybór: ")
    if jezyk =="polskie":
        fiszki_polskie(polskie, francuskie)
    elif jezyk == "francuskie":
        fiszki_francuskie(polskie, francuskie)
    else:
        print("Błednie wpisane")

def fiszki_polskie(polskie, francuskie):
    while len(francuskie) > 0:
        if len(polskie) > 0:
            position = random.randint(0, len(polskie)-1)
        else:
            print("Super! Wszystkie fiszki zostały powtórzone!")
            return       
        print(polskie[position])
        odpowiedz = input("Podaj tłumaczenie: ")
        if odpowiedz.lower() == francuskie[position].lower():
            print("Dobrze!")
            francuskie.pop(position)
            polskie.pop(position)
        else:
            print(francuskie[position])
    print("Fiszki skończone")

def fiszki_francuskie(polskie, francuskie):
    while len(polskie) > 0:
        if len(francuskie) > 0:
            position = random.randint(0, len(francuskie)-1)
        else:
            print("Super! Wszystkie fiszki zostały powtórzone!")
            return        
        print(francuskie[position])
        odpowiedz = input("Podaj tłumaczenie: ")
        if odpowiedz.lower() == polskie[position].lower():
            print("Dobrze!")
            francuskie.pop(position)
            polskie.pop(position)
        else:
            print(polskie[position])
    print("Fiszki skończone")

def dodaj_haslo(plword, frword):
    if plword=="" or frword=="":
        return
    file = open('words.txt', 'a', encoding='utf-8')
    file.write(plword+";"+frword + "\n")
    file.close()
    #print("Zapisałaś: "+ plslowo.strip() + " - " + frslowo.strip())

def usun_haslo(plword, frword):
    slowo = input("Podaj francuskie hasło które chcesz usunąć: ")
    if slowo not in francuskie:
        print("Nie ma takiego słowa")
        return
    position = francuskie.index(slowo)
    tlumaczenie = polskie[position]
    with open('words.txt', 'r', encoding='utf-8') as file:
        linijki = file.readlines()
    if 0 <= position < len(linijki):
        del linijki[position]
    with open('words.txt', 'w', encoding='utf-8') as plik:
        plik.writelines(linijki)

    with open('fiszki_storage.txt', 'a', encoding='utf-8') as plik:
        plik.write(slowo+";"+tlumaczenie+"\n")

def czy_jest(polskie, francuskie):
    haslo = input("Podaj hasło:  ")
    if check(francuskie, haslo) == True:
        print("Tak, haslo jest w bazie")
    else:
        print("Nie ma takiego hasła")
def wczytaj_slowa():
    francuskie = []
    polskie = []
    with open('words.txt', 'r', encoding='utf-8') as words:#with open sam zamyka plik
        for line in words:
            pol, fran = line.strip().split(";")
            polskie.append((pol))
            francuskie.append(( fran))
    francuskie = [str(x.strip()) for x in francuskie]
    polskie = [str(x.strip()) for x in polskie]
    return polskie, francuskie

'''
polskie, francuskie = wczytaj_slowa()
print("Co chcesz zrobić? Wybierz: fiszki/dodaj haslo/usun haslo/czy jest/end")
decyzja = input("Wybór: ")

if decyzja == "fiszki usuwane":
    fiszki(polskie, francuskie)

elif  decyzja == "dodaj haslo":
    dodaj_haslo(polskie, francuskie)

elif decyzja == "usun haslo":
    usun_haslo(polskie, francuskie)

elif decyzja == "czy jest":
    czy_jest(polskie, francuskie)
        
elif decyzja == "end":
    print("Nie ma takiego słowa")
    '''