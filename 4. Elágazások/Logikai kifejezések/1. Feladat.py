'''
1. Feladat
Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót.
'''

szam = int(input('Adj meg egy egész számot: '))

if szam % 2 == 0 and szam > 0:
    print(f'A megadott szám ({szam}) pozitív páros')

elif szam % 2 != 0 and szam < 0:
    print(f'A megadott szám ({szam}) negatív páratlan.')

else:
    print(f'A megadott szám ({szam}) nem -pozitív páros vagy -negatív páratlan.')
