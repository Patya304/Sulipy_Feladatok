'''
1. Feladat - Pocak
Készíts egy programot while ciklussal , amely a felhasználótól bekér egy páros számot, majd ennek megfelelően rajzol ki a képernyőre egy pocak szerű alakzatot az alábbiak szerint!
'''

szam = int(input("Kérek egy páros számot: "))
sor = 1

while szam % 2 == 1:
  szam = int(input("Páros szám kell: "))

while sor <= szam / 2:
  print(sor*'O ')
  sor+=1
sor = 0
while sor < szam / 2:
  print((int)(szam/2-sor)*'O ')
  sor+=1