feladat=1
while feladat <=20:
    import random
    szam = random.randint (2,60)
    szam1 =random.randint (1,40)
    mateklecke=True
    print('csináld meg az összeadást')
    while mateklecke:
        print(szam, '+', szam1)
        osszeg=int(input('Számok összege?\t'))
        if osszeg==szam+szam1:
            mateklecke=False
            print('Ügyes voltál!\t')
        else: print("na még egyszer!", end='\t')
    feladat=feladat+1     