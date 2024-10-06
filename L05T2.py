OIKEA_VASTAUS = 33
def tulostaOhjeet():
    print("Tällä ohjelmalla voit arvata lukua.\nOhjelma kertoo onko arvauksesi pienempi vai suurempi kuin arvattava kokonaisluku.\n")
    return None
def kysyLuku(kehote):
    luku = int(input(kehote))
    return(luku)
def tarkistaLuku(arvaus, arvaukset):
    if arvaus == OIKEA_VASTAUS:
        print("Arvasit oikein! Onneksi olkoon!\nKäytit",arvaukset,"arvausta.")
        return True
    elif abs(OIKEA_VASTAUS - arvaus )<5:
        print("Olet jo lähellä! Yritä uudelleen.")
        return False
    elif arvaus <  OIKEA_VASTAUS:
        print("Luku on vähintään 5 suurempi kuin arvaus. Yritä uudelleen.")
        return False
    elif arvaus > OIKEA_VASTAUS:
        print("Luku on vähintään 5 pienempi kuin arvaus. Yritä uudelleen.")
        return False
    return None
def paaohjelma():
    arvaukset = 1
    oikein = False
    tulostaOhjeet()
    while oikein == False:
        arvaus = kysyLuku("Anna arvauksesi luvusta: ")
        oikein = tarkistaLuku(arvaus, arvaukset)
        arvaukset += 1
    print("Kiitos ohjelman käytöstä.")
    return None
paaohjelma()