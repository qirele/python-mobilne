o1 = int(input("Liczba osób w przepisie:"))

s1 = float(input("Ile skladnikow dla 1 osoby:"))

o2 = int(input("Liczba uczestnikow:"))

print("dla " + str(o2) + " osob potrzeba: " + str(s1/o1* o2) + " skladnika")