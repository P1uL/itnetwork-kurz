
from spravapojisteni import SpravaPojisteni

sprava_pojisteni = SpravaPojisteni()


while True:
    print("---------------------------\n "
        "Evidencia pojištěných\n"
        "---------------------------")


    print("Vyberte si akci:")
    print("1 - Přidat nového pojištěného")
    print("2 - Vypsat všechny pojištěné")
    print("3 - Vyhledat pojištěného")
    print("4 - Konec")

    volba = input("Zadejte volbu: \n")




    if volba == "1":
        jmeno = input("Zadejte jméno pojištěného: ")
        prijmeni = input("Zadejte příjmení: ")
        vek = int(input("Zadejte věk: "))
        telefon = input("Zadejte telefonní číslo: ")
        sprava_pojisteni.pridej_pojisteneho(jmeno, prijmeni, vek, telefon)
        print("\nPojištěný byl úspěšně přidán.")




    elif volba == "2":
        print("\nSeznam pojištěných:\n")
        sprava_pojisteni.zobraz_seznam_pojistenych()




    elif volba == "3":
        jmeno = input("Jméno: ")
        prijmeni = input("Příjmení: ")
        vyhledany = sprava_pojisteni.vyhledej_pojisteneho(jmeno, prijmeni)
        if vyhledany:
            print("\nVyhledaný pojištěný:")
            print(vyhledany)
        else:
            print("Pojištěný nebyl nalezen.")




    elif volba == "4":
        print("Program byl ukončen.")
        break

    else:
        print("Neplatná volba. Zkuste to znovu.")







