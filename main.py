def arnovekedes(darab):
    if darab == 0:
        return 0
    elif darab == 1:
        return 1000
    elif darab == 2:
        return 1000+900
    else:
        return (darab-2)*900+1900
vasarlas1 = []
vasarlas2 = {}
fajl = open('kosar.txt')
print('1. feladat: A kosar.txt beolvasása.')
for sor in fajl:
    sor = sor.strip()
    if sor == 'F':
        vasarlas1.append(vasarlas2)
        vasarlas2 = {}
    else:
        vasarlas2[sor] = vasarlas2.get(sor, 0) + 1
fajl.close()
print('2. feladat:', len(vasarlas1), ' alkalommal fizettek a pénztárnál.')
sorszam = int(input('3. feladat: Adja meg a vásárlás sorszámát! '))
print(sum(vasarlas1[sorszam].values()), 'termék volt a kosarában')
print('A kosár tartalma:',)
for arucikk, vasarolt_db in vasarlas1[sorszam - 1].items():
    print(vasarolt_db, arucikk)
"""print('A vásárlás összege: ', arnovekedes(vas_db), sep='')
print('\nA vásárlás összege: ', sum(vasarlas1[sorszam]))"""
cikk_nev = input('4. feladat: Adja meg az árucikk nevét! ')
vettek_ilyet = [index + 1 for index, vas in enumerate(vasarlas1) if cikk_nev in vas.keys()]
print('Első vásárlás sorszáma: ', vettek_ilyet[0], '\nUtolsó vásárlás sorszáma: ', vettek_ilyet[-1],
      '\n', len(vettek_ilyet), ' alkalommal vásároltak az árucikkből.', sep='')
infajl = open('osszeg.txt', 'w')
for index, vasarlas2 in enumerate(vasarlas1):
    print(index + 1, ': ', sum(map(arnovekedes, vasarlas2.values())), sep='', file=infajl)
infajl.close()
print("5. feladat: A vásárlások összegének mentése az osszeg.txt fájlba.")