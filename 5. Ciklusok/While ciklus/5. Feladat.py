'''
5. Feladat
Írj egy programot while ciklussal, amely a felhasználótól páros számot kér be. Amennyiben a megadott szám páratlan, újra és újra megtörténik az adatbekérés mindaddig, amíg végül páros számot nem ad meg a felhasználó.
'''

szam = int(input("Kérek egy páros számot: "))
if szam % 2 == 0:
    print("Fasza gyerek vagy te!")

while szam % 2 == 1:
    szam = int(input("Látom nem tudod a páros és a páratlan számokat, írj be egy párosszámot!: "))
    if szam % 2 == 0:
      print("Na végre sikerült. Tudtam hogy fasza gyerek vagy te!")