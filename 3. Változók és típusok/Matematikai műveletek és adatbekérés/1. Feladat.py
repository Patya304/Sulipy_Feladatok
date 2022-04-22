'''
1. Feladat
Készíts egy rövid programot, amely a felhasználótól bekéri a kör sugarát, és ennek alapján kiszámolja a kör kerületét és területét!
'''

import math

r = int(input('Add meg a kör sugarát: '))

kor_t = r**2 * math.pi
print('A kör terültete:', kor_t)

kor_k = 2 * r * math.pi
print('A kör kerülte:', kor_k)