def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Kysy merkki ja kuvion koko")
    print("2) Tulosta neliö")
    print("3) Tulosta kolmio")
    print("0) Lopeta")
    valinta = input("Anna valintasi: ")
    return int(valinta)

def kysySyote(kehotus):
    syote = input(kehotus)
    return syote

def tulostaKolmio(koko, merkki):
    for i in range(1, koko + 1):
        line = ''
        for j in range(1, i + 1):
            line += merkki + ' '
        print(line)
    print("")
    return None

def tulostaNelio(koko, merkki):
    for i in range(koko):
        line = ''
        for j in range(koko):
            line += merkki + ' '
        print(line)
    print("")
    return None

def paaohjelma():
    print("Tämä ohjelma tulostaa käyttäjän antaman syötteen mukaisia muotoja.")
    koko = 0
    merkki = ''
    while True:
        valinta = valikko()
        if valinta == 1:
            koko_str = kysySyote("Anna tulostettavan muodon koko: ")
            koko = int(koko_str)
            merkki = kysySyote("Anna muodon tulostuksessa käytettävä merkki: ")
            print("")
        elif valinta == 2:
            tulostaNelio(koko, merkki)
        elif valinta == 3:
            tulostaKolmio(koko, merkki)
        elif valinta == 0:
            print("Lopetetaan.")
            print("\nKiitos ohjelman käytöstä.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")
    return None

paaohjelma()
