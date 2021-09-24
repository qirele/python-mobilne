import math

dlug = float(input("dlugosc: "))
szer = float(input("szerokosc: "))

paczka = float(input("metry na jedna paczke: "))

wynik = dlug * szer / paczka
print("Liczba panel: " + str(math.ceil(wynik)))