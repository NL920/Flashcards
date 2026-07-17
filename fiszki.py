#przerobić na -funkcje pod flask
import random
import sys

def czy_jest(lista, haslo):
    for elem in lista:
        if elem.lower() == haslo.lower():
            return True
    return False


with open('polskie.txt', 'r', encoding='utf-8') as filepl:#with open sam zamyka plik
    polskie = filepl.readlines()
with open('francuskie.txt', 'r', encoding='utf-8') as filefr:
    francuskie = filefr.readlines()   
francuskie =  [str(x.strip()) for x in francuskie]
polskie = [str(x.strip()) for x in polskie]

# dodać wprowadzenie
print("Co chcesz zrobić? Wybierz: fiszki usuwane/fiszki nieusuwane /dodaj haslo/usun haslo/czy jest/end")
decyzja = input("Wybór: ")
print(francuskie)
if decyzja == "fiszki nieusuwane":
    wyn = "next"
    while wyn != "end":
        position = random.randint(0, len(polskie)-1)
        print(polskie[position])
        odpowiedz = input("Podaj tłumaczenie: ")
        if odpowiedz == francuskie[position]:
            print("Dobrze!")
        else:
            print(francuskie[position])
        wyn = input("Jeżeli chcesz zakończyć napisz end, jeżeli nie napisz next: ")

elif decyzja == "fiszki usuwane":
    print("Hasła po polsku czy po francusku: polskie/francuskie ")
    jezyk = input("Wybór: ")
    if jezyk =="polskie":
        while len(francuskie) > 0:
            if len(polskie) > 0:
                position = random.randint(0, len(polskie)-1)
            else:
                print("Super! Wszystkie fiszki zostały powtórzone!")
                sys.exit()        
            print(polskie[position])
            odpowiedz = input("Podaj tłumaczenie: ")
            if odpowiedz.lower() == francuskie[position].lower():
                print("Dobrze!")
                francuskie.pop(position)
                polskie.pop(position)
            else:
                print(francuskie[position])
        print("Fiszki skończone")
    elif jezyk == "francuskie":
        while len(polskie) > 0:
            if len(francuskie) > 0:
                position = random.randint(0, len(francuskie)-1)
            else:
                print("Super! Wszystkie fiszki zostały powtórzone!")
                sys.exit()        
            print(francuskie[position])
            odpowiedz = input("Podaj tłumaczenie: ")
            if odpowiedz.lower() == polskie[position].lower():
                print("Dobrze!")
                francuskie.pop(position)
                polskie.pop(position)
            else:
                print(polskie[position])
        print("Fiszki skończone")
    else:
        print("Błednie wpisane")

elif  decyzja == "dodaj haslo":
    filefr = open('francuskie.txt', 'a', encoding='utf-8')
    filepl =  open('polskie.txt', 'a', encoding='utf-8')
    print("Podaj francuskie słowo: ")
    frslowo = input("Slowo: ")
    print("Podaj polskie tłumaczenie: ")
    plslowo = input("Slowo: ")
    frslowo = frslowo 
    plslowo = plslowo
    filefr.write(frslowo + "\n")
    filepl.write(plslowo + "\n")
    filepl.close()
    filefr.close()
    print("Zapisałaś: "+ plslowo.strip() + " - " + frslowo.strip())

elif decyzja == "usun haslo":
    slowo = input("Podaj francuskie hasło które chcesz usunąć")
    if slowo not in francuskie:
        print("Nie ma takiego słowa")
        sys.exit()
    position = francuskie.index(slowo)
    tlumaczenie = polskie[position]
    with open('francuskie.txt', 'r', encoding='utf-8') as filefr:
        linijki = filefr.readlines()
    if 0 <= position < len(linijki):
        del linijki[position]
    with open('francuskie.txt', 'w', encoding='utf-8') as plik:
        plik.writelines(linijki)

    with open('polskie.txt', 'r', encoding='utf-8') as filepl:
        linijki = filepl.readlines()
    if 0 <= position < len(linijki):
        del linijki[position]
    with open('polskie.txt', 'w', encoding='utf-8') as plik:
        plik.writelines(linijki)
    with open('fiszki_storage.txt', 'a', encoding='utf-8') as plik:
        plik.write(slowo+";"+tlumaczenie)
elif decyzja == "czy jest":
    haslo = input("Podaj hasło:  ")
    if czy_jest(francuskie, haslo) == True:
        print("Tak, haslo jest w bazie")
    else:
        print("Nie ma takiego hasła")
elif decyzja == "end":
    sys.exit()