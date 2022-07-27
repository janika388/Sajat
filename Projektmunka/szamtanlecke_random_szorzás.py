feladat=1
while feladat <=20:
    import random
    szam = random.randint (1,9)
    szam1 =random.randint (1,8)
    mateklecke=True
    print('Szorozd meg a két számot')
    while mateklecke:
        print(szam, '*', szam1)
        osszeg=int(input('Számok szorzata?\t'))
        if osszeg==szam*szam1:
            mateklecke=False
            print('Ügyes voltál!\t')
        else: print("Na még egyszer!", end='\t')
    feladat=feladat+1     