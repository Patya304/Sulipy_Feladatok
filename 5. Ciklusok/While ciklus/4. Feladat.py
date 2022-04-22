'''
4. Feladat
Írj egy programot while ciklussal, amely a felhasználó által meghatározott alkalommal írja ki a bekért szöveget!
'''

szam = int(input('Kérek egy számot: '))
szoveg = input('Kérek egy szöveget: ')

x = 0
while x < szam:
  print(szoveg)
  x += 1
