'''
2. Feladat
Írj egy programot, ami a felhasználótól bekéri először a keresztnevét, majd a vezetéknevét. A program ezután összefűzi ezeket egy teljes_nev nevű változóba. Végül a program a teljes nevén üdvözli a felhasználót!
'''

k_nev = input('Kérlek mondd meg a keresztneved: ')
print('Szia', k_nev)

v_nev = input('Kérlek mondd meg a vezetékneved: ')
print(v_nev)

teljes_nev = print(f'Köszöntelek a python világában {v_nev} {k_nev}.!')