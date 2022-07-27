feladat=1
while feladat <=20:
    import random
    szam = random.randint (1,80)
    szam1 =random.randint (1,40)
    mateklecke=True
    
    while szam%szam1==0:
        print('Oszd el a két számot')
        szamolas=True
        while mateklecke:
            print(szam, '/', szam1)
            osszeg=int(input('Számok osztója?\t'))
            if osszeg==szam/szam1:
                mateklecke=False 
                print('Ügyes voltál!\t')
            else: print("Na még egyszer!", end='\t')
        szamolas=False 
    feladat=feladat+1
               
        
