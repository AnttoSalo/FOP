def valikko():
    print("Valitse haluamasi toiminto:")
    print("1) Laske aritmeettinen sarja")
    print("2) Laske geometrinen sarja")
    print("0) Lopeta")
    valinta = input("Anna valintasi: ")
    return valinta

def kysyLuku(kehotus):
    luku = int(input(kehotus))
    return luku

def aritmeettinen(alku, d, n):
    summa = 0
    for i in range(n):
        termi = alku + i * d
        print(termi,end=" ")
        summa += termi
    print("\nAritmeettisen sarjan summa on",str(summa)+".\n")
    return None

def geometrinen(alku, r, n):
    summa = 0
    for i in range(n):
        termi = alku * (r ** i)
        print(termi, end=" ")
        summa += termi
    print("\nGeometrisen sarjan summa on", str(summa) + ".\n")
    return None

def paaohjelma():
    print("Tämä ohjelma laskee aritmeettisen tai geometrisen sarjan.")
    while True:
        valinta = int(valikko())
        if valinta == 0:
            print("Lopetetaan.\n\nKiitos ohjelman käytöstä.")
            return None
        elif valinta == 1:
            alku = kysyLuku("Anna sarjan alkuarvo: ")
            n = kysyLuku("Anna n: ")
            d = kysyLuku("Anna d: ")
            aritmeettinen(alku, d, n)
        elif valinta == 2:
            alku = kysyLuku("Anna sarjan alkuarvo: ")
            n = kysyLuku("Anna n: ")
            r = kysyLuku("Anna r: ")
            geometrinen(alku, r, n)
        else:
            print("Tuntematon valinta, yritä uudestaan.\n")
    return None

paaohjelma()