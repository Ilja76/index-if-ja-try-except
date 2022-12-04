

#arv=input("Arv")


#try:
#    arv=int(arv)
#    print("Int")

#except:
#    try:
#        arv=float(arv)
#        print("Float")
#    except:
#        print("Tekst")

from math import *

print("Ulesanne 1")
print("Tere! Olen sinu uus s�ber - Python!")
nimi=input("Sinu nimi: ")
print("Oi, kui ilus nimi!")

a=input("Kas sa tahad sinu keha indeksi? 0-ei, 1-jah ")
if a=="1":
    while True:
        try:
            pikkus=int(input("Pikkus: "))
            if pikkus>0 and pikkus<273: break
        except:
            print("Error")
    mass=-1
    while mass<0 or mass>400:
        try:
            mass=int(input("Mass: "))
        except:
            print("Error")
        i=round(mass/(0.01*pikkus)**2,1)
        print("Sinu keha indeks on:")
        print(i)
    if i<=16:
        print("Tervisele ohtlik alakaal")
    elif i>16 and i<=19:
        print("Alakaal")
    elif i>19 and i<=25:
        print("Normaalkaal")
    elif i>25 and i<=30:
        print("�lekaal")
    elif i>30 and i<=35:
        print("Rasvumine")
    elif i>35 and i<=40:
        print("Tugev rasvumine")
    elif i>40:
        print("Tervisele ohtlik rasvumine")
    print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
else:
    print("GoodBye!")

