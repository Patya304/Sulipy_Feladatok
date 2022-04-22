'''
1. Feladat
Írj egy programot while ciklussal amely kiírja a páros számokat 1 és 10 között!
'''

szam = 1
while szam <= 10:
    if szam % 2 == 0:
      print(szam)
    szam += 1