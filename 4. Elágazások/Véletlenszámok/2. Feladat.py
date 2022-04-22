'''
2. Feladat
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
'''

fej_valt = 'fej'

iras_vat = 'írás'

szo = input('fej vagy írás: ')

if szo == 'fej':
    print('Eltaláltad!')

elif szo == 'írás':
    print('Eltaláltad!')

else:
    print('Nem értelmezem az általad megadott karaktert.')