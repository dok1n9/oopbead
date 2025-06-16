from abc import ABC, abstractmethod


class Jarat(ABC):

    @abstractmethod
    def __init__(self, lajstrom, vegcel, szhely:int):
        self.lajstrom=lajstrom
        self.vegcel=vegcel
        self.szhely=szhely

    @abstractmethod
    def jegyar(self):
        pass

class BelfoldiJarat(Jarat):
    
    def __init__(self, bosztaly, lajstrom, vegcel, szhely):
        super().__init__(lajstrom, vegcel, szhely)
        self.bosztaly=bosztaly
        self.alapar=20000

    def jegyar(self):
        return self.alapar/self.bosztaly

class NemkoziJarat(Jarat):

    
    def __init__(self, nosztaly, lajstrom, vegcel, szhely):
        super().__init__(lajstrom, vegcel, szhely)
        self.nosztaly=nosztaly
        self.alapar=50000

    def jegyar(self):
        return self.alapar/self.nosztaly

class Jegyek:
    
    def __init__(self, jarat, utasneve, datum):
        self.jarat = jarat
        self.utasneve = utasneve
        self.datum = datum
        self.ar = jarat.jegyar()

class Adatok:
    
    def __init__(self):
        self.jaratok = []
        self.foglalasok = []
    
    def __add__(self,jarat):
        self.jaratok.append(jarat)
        return self

    def jaratlista(self):
        for j in self.jaratok:
            print(f"{j.lajstrom} jelzésű gép- {j.vegcel} uticéllal - {j.szhely} szabadhellyel rendelkezik.")

    def ujfoglalasok(self, jarat, utasneve, datum):
        ujfoglalas = Jegyek(jarat, utasneve, datum)
        self.foglalasok.append(ujfoglalas)
        
        return ujfoglalas
    
    def lemondas(self, jarat, utasneve):
        for l in self.foglalasok:
            if l.jarat==jarat and l.utasneve==utasneve:
                    self.foglalasok.remove(l)
                    print ("Foglalás törölve.")
                    return True
        print ("Nincs ilyen foglalás.")
        return False
 
    def foglalolista(self):
        for f in self.foglalasok:
            print(f"{f.utasneve} -> {f.jarat.vegcel} ({f.datum}) | Ár: {f.ar} Ft")

class LegiTars():
    
    def __init__(self, nev):
        self.nev=nev
