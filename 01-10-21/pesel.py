def czyParzysta(liczba):
    if liczba % 2 == 0:
        return True
    else: 
        return False


def kto(pesel):
    plec = pesel[9]
    if czyParzysta(int(plec)):
        print("Kobieta")
    else:
        print("Mezczyzna")


pesel = input("Podaj pesel (11 liter): ")
while len(pesel) != 11:
    pesel = input("Podaj pesel (11 liter): ")

kto(pesel)
