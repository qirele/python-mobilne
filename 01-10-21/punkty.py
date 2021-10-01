punkty = int(input("Podaj liczbe zdobytych punktow klasy: "))
while punkty < 0:
    punkty = int(input("Podaj liczbe zdobytych punktow klasy (p > 0): "))

frekw = float(input("Podaj frekwencje klasy: "))
while frekw < 0:
    frekw = float(input("Podaj frekwencje klasy (f > 0): "))
    
sredniaOcen = float(input("Podaj srednia ocen klasy: "))
while sredniaOcen < 0:
    sredniaOcen = float(input("Podaj srednia ocen klasy (s > 0): "))
    


if frekw > 94 and sredniaOcen > 4:
    punkty = punkty + 20
    
print("Aktualna liczba punktow wynosi: ", punkty)
