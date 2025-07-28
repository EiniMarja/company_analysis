# Määritellään Pelikortti-luokka
class Pelikortti:
    def __init__(self, maa, arvo):
        self.maa = maa
        self.arvo = arvo

# Luodaan viisi pelikortti-oliota
kortti1 = Pelikortti("Pata", 1)
kortti2 = Pelikortti("Ruutu", 10)
kortti3 = Pelikortti("Hertta", 11)
kortti4 = Pelikortti("Risti", 7)
kortti5 = Pelikortti("Ruutu", 13)

# Tulostetaan ominaisuudet
print(kortti1.maa + ", " + str(kortti1.arvo))
print(kortti2.maa + ", " + str(kortti2.arvo))
print(kortti3.maa + ", " + str(kortti3.arvo))
print(kortti4.maa + ", " + str(kortti4.arvo))
print(kortti5.maa + ", " + str(kortti5.arvo))
