feladat=1
while feladat <=20:
    import random
    szam = random.randint (3,10)
    szam1 =random.randint (5,9)
    mateklecke=True
    print('Csináld meg az összeadást')
    while mateklecke:
        print(szam, '+', szam1)
        osszeg=int(input('Számok összege?\t'))
        if osszeg==szam+szam1:
            mateklecke=False
            print('Ügyes voltál!\t')
        else: print("Na még egyszer!", end='\t')
    feladat=feladat+1
print('Vége')