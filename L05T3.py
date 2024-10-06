VOKAALIT = "aeiouyäö"

def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Kysy merkkijono")
    print("2) Analysoi merkkijono")
    print("3) Tulosta tulokset")
    print("0) Lopeta")
    valinta = input("Anna valintasi: ")
    return valinta

def kysyMerkkijono():
    merkkijono = input("Anna merkkijono: ")
    print("")
    return merkkijono

def analysoi(merkkijono):
    tuloste = ""
    tuloste += "Merkkijono on " + str(len(merkkijono)) + " merkkiä pitkä.\n"
    tuloste += "Merkkijono takaperin on '" + merkkijono[::-1] + "'.\n"
    if merkkijono[0].lower() in VOKAALIT:
        tuloste += "Merkkijonon '" + merkkijono + "' ensimmäinen kirjain '" + merkkijono[0] + "' on vokaali.\n"
    else:
        tuloste += "Merkkijonon '" + merkkijono + "' ensimmäinen kirjain '" + merkkijono[0] + "' on konsonantti.\n"
    print("Analyysi suoritettu merkkijonolle '" + merkkijono + "'.\n")
    return tuloste

def tulostaTulokset(tuloste):
    print(tuloste)
    return None

def paaohjelma():
    tuloste = ""
    while True:
        valinta = int(valikko())
        if valinta == 0:
            print("Lopetetaan.\n\nKiitos ohjelman käytöstä.")
            break
        elif valinta == 1:
            merkkijono = kysyMerkkijono()
        elif valinta == 2:
            tuloste = analysoi(merkkijono)
        elif valinta == 3:
            tulostaTulokset(tuloste)
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")
    return None
paaohjelma()