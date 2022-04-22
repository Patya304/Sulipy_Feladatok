'''
1. Feladat
Thonny fejlesztői környezetben készíts egy rövid programot, amely
kommentként tartalmazza a program funkciójának leírását,
konstansként tárolja PI értékét,
egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
kiszámolja és a képernyőre kiírja a kör kerületét és területét!
[Megjegyzés] A szorzás jele: *
'''

import math

r = int(input('Add meg a kör sugarát: '))

kor_t = r**2 * math.pi
print('A kör terültete:', kor_t)

kor_k = 2 * r * math.pi
print('A kör kerülte:', kor_k)
