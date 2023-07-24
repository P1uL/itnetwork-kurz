from pojisteny import Pojisteny

class SpravaPojisteni:
    def __init__(self):
        self.pojisteni = []

    def pridej_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.pojisteni.append(pojisteny)

    def zobraz_seznam_pojistenych(self):
        if self.pojisteni:
            for pojisteny in self.pojisteni:
                print(pojisteny)
        else:
            print("Žádní pojištění nebyli evidováni.")

    def vyhledej_pojisteneho(self, jmeno, prijmeni):
        for pojisteny in self.pojisteni:
            if pojisteny.jmeno == jmeno and pojisteny.prijmeni == prijmeni:
                return pojisteny

  



