def tulostaOhjeet():
    print("Tämä ohjelma kysyy ja tulostaa tietoja.\nTämä aliohjelma tulostaa ohjeita käyttäjälle.\nAnna ensin kaksi lukua.")
    return None
def kysyLuku(ensimmainen):
    print("Tämä aliohjelma kysyy kokonaisluvun.")
    if ensimmainen:
        luku = int(input("Anna ensimmäinen luku: ")) 
    else:
        luku = int(input("Anna toinen luku: ")) 
    return(luku)
def tulostaTulokset(luku1,luku2):
    print("Tämä aliohjelma tulostaa lukujen summan ja summan parillisuuden.")
    summa = luku1 + luku2
    print(luku1,"+",luku2,"=",summa)
    if summa % 2 == 0:
        print(summa,"on parillinen luku.")
    else:
        print(summa, "ei ole parillinen luku.")
    return None
def paaohjelma():
    tulostaOhjeet()
    luku1 = kysyLuku(True)
    luku2 = kysyLuku(False)
    tulostaTulokset(luku1,luku2)
    print("Kiitos ohjelman käytöstä.")
    return None

paaohjelma()