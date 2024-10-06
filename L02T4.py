merkkijono = input("Anna kurssikoodi ja nimi: ")

print("Antamasi merkkijono '" + merkkijono + "' oli " + str(len(merkkijono)) + " merkkiä pitkä.\n")
kurssikoodi = merkkijono[:9]
print("Pelkkä kurssikoodi on " + kurssikoodi)

kurssinimi = merkkijono[10:]
print("Pelkkä kurssinimi on " + kurssinimi)

print("Merkkijonon merkit 4, 5, 6 ja 7 ovat " + merkkijono[3:7] + "\n")
print("Merkkijonon joka kolmas merkki alkaen ensimmäisestä merkistä: " + merkkijono[::3] + "\n")
print("Merkkijono takaperin on: " + merkkijono[::-1] + "\n")

aloitus = int(input("Anna aloituspaikka: "))
lopetus = int(input("Anna lopetuspaikka: "))
siirtyma = int(input("Anna siirtymä: "))

print("Merkkijono antamillasi syötteillä tulostuu näin: " + merkkijono[aloitus:lopetus:siirtyma] + "\n")

print("Kiitos ohjelman käytöstä.")
