'''
3. Feladat
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
'''
import random

random_szam = random.randint(1, 5)
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
