"""
1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""

import random

random_szam = random.randint(1, 3)
print(f'A gép választása: {random_szam}')

szam = int(input('Adj meg egy számot: '))

if szam == random_szam:
    print(
        f'Az általad megadott szám ({szam}), egyenlő a gép által választott számmal ({random_szam}).'
    )

elif szam > random_szam:
    print(
        f'Az általad megadott szám ({szam}), nagyobb a gép által választott számnál ({random_szam}).'
    )

else:
    print(
        f'Az általad megadott szám ({szam}), kisebb a gép által választott számnál ({random_szam}).'
    )
  