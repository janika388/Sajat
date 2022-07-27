feladat=1
while feladat <=20:
    import random
    szam = random.randint (1,30)
    szam1 =random.randint (1,30)
    mateklecke=True
    print('Végezd el a kivonást')
    if szam >= szam1:
        while mateklecke:
            print(szam, '-', szam1)
            osszeg=int(input('Számok Különbsége?\t'))
            if osszeg==szam-szam1:
                mateklecke=False
                print('Ügyes voltál!\t')
            else: print("Na még egyszer!", end='\t')
        feladat=feladat+1
    else:
        while mateklecke:
            print(szam1, '-', szam)
            osszeg=int(input('Számok Különbsége?\t'))
            if osszeg==szam1-szam:
                mateklecke=False
                print('Ügyes voltál!\t')
            else: print("Na még egyszer!", end='\t')
        feladat=feladat+1
