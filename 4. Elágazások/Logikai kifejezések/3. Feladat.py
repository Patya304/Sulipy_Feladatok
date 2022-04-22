'''
3. Feladat
Készíts egy programot, amely a felhasználó által megadott egész számról eldönti, hogy
- csak 3-mal osztható,
- csak 4-gyel osztható,
- 3-mal és 4-gyel is osztható,
- sem 3-mal, sem 4-gyel nem osztható!
'''

szam = int(input('Kérek egy számot: '))
harommal = szam % 3 == 0
neggyel = szam % 4 == 0

if harommal and neggyel:
    print('3-mal és 4-gyel is oszható! ')
elif harommal:
    print('csak 3-mal osztható!')
elif neggyel:
    print('csak 4-gyel oszható!')
else:
    print('sem 3-mal, sem 4-gyel nem osztható!')