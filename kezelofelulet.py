from beadclass.adatok import Adatok
from beadclass.adatok import BelfoldiJarat
from beadclass.adatok import NemkoziJarat
from beadclass.adatok import LegiTars


lt=LegiTars("SkyWays")
adatok=Adatok()

bjarat1=BelfoldiJarat(1, "HA-111", "Airbus A320", "Debrecen", 15000)
bjarat2=BelfoldiJarat(2, "HA-112", "Airbus A320", "Budapest", 10000)
njarat1=NemkoziJarat(1, "HA-221", "Boeing 777", "London", 25000)
njarat2=NemkoziJarat(2, "HA-222", "Boeing 777", "Budapest", 20000)

adatok+bjarat1
adatok+bjarat2
adatok+njarat1
adatok+njarat2

foglalas1=adatok.ujfoglalasok(njarat1, "Utas1", "2025-06-01")
foglalas2=adatok.ujfoglalasok(njarat2, "Utas2", "2025-06-02")
foglalas3=adatok.ujfoglalasok(bjarat2, "Utas3", "2025-06-03")

print()
print ("Üdvözöljük a Liszt Ferenc Repülőtér honlapján.")

while True:
    print()
    print("Kérem válasszon az alábbi menüpontok közül.")
    print("1 - Foglalások.")
    print("2 - Járatok listázása.")
    print("3 - Kilépés.")
    print()

    valasz=int(input("Választott menüpont: "))

    if valasz==1:
        while True:
            print()
            print ("Kérem válasszon az alábbi menüpontok közül.")
            print("1 - Új foglalás.")
            print("2 - Foglalások törlése.")
            print("3 - Foglalások listázása.")
            print("4 - Visszalépés a főmenübe.")
            print()

            valaszfog=int(input("Választott menüpont: "))

            if valaszfog==1: #Új foglalás
                adatok.jaratlista()
                lajstrom=input("Kérem adja meg a járat lajstromszámát (pl. AA-000): ")
                datum=input("Adja meg az utazás dátumát (pl. 2025-06-01): ")
                utas=input("Adja meg a nevét: ")
                jarat=next((j for j in adatok.jaratok if j.lajstrom==lajstrom), None)
 
                if jarat:
                    adatok.ujfoglalasok(jarat, utas, datum)
                    print("Foglalás rögzítve.")
                    adatok.foglalolista()
                
                else:
                    print("Nincs ilyen járat.")

            elif valaszfog==2: #Foglalások törlése
                adatok.foglalolista()
                datum=input("Adja meg az utazás dátumát (pl. 2025-06-01): ")
                utas=input("Kérem adja meg a nevét: ")
                lemond=next((f for f in adatok.foglalasok if f.datum==datum and f.utasneve == utas), None)

                if lemond:
                    adatok.foglalasok.remove(lemond)
                    print("Foglalás törölve.")
                    adatok.foglalolista()
                
                else:
                    print("Nincs ilyen járat.")
            
            elif valaszfog==3:
                adatok.foglalolista()

            elif valaszfog==4:
                print("Visszalépés...")
                break

            else:
                print("Nincs ilyen menüpont.")
    
    elif valasz==2:
        adatok.jaratlista()

    elif valasz==3:
        print("Kilépés...")
        break

    else:
        print("Nincs ilyen menüpont.")