'''
6. Feladat
Írj egy programot, amely [1;12] intervallumon állít elő 20 darab véletlenszámot! A képernyőre kizárólag csak a 3-mal oszthatóakat írja ki, és a végén informálja a felhasználót arról is, hány darab ilyen szám volt.
'''

import random

i = 0
temp = 0
while i < 20:
  a = random.randint(1, 12)
  if a % 3 ==0:
    print(a)
    temp+=1
  i+=1

print(f"Összesen 20-számot generáltam ebből 3-mal oszható: {temp} szám")