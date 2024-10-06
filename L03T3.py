print("Tämä on valikkopohjainen ohjelma, jossa voit valita haluamasi toiminnon.")

merkkijono = input("Anna merkkijono, josta haluat selvittää tietoja: ")

print("\nValitse haluamasi toiminto:")
print("1) Tulosta merkkijonon kolme ensimmäistä kirjainta")
print("2) Selvitä tuleeko merkkijonon ensimmäinen vai viimeinen merkki aakkosissa ensin")
print("3) Tulosta merkkijono väärinpäin")
print("0) Lopeta")

valinta = input("Anna valintasi: ")
print("")
if valinta == "1":
    print("Merkkijonon kolme ensimmäistä merkkiä ovat '" + merkkijono[:3] + "'.")
elif valinta == "2":
    if merkkijono[0].lower() < merkkijono[-1].lower():
        print("Merkkijonon ensimmäinen merkki '" + merkkijono[0] + "' tulee aakkosissa ennen merkkijonon viimeistä merkkiä '" + merkkijono[-1] + "'.")
    elif merkkijono[0].lower() > merkkijono[-1].lower():
        print("Merkkijonon viimeinen merkki '" + merkkijono[-1] + "' tulee aakkosissa ennen merkkijonon ensimmäistä merkkiä '" + merkkijono[0] + "'.")
    else:
        print("Merkkijonon ensimmäinen ja viimeinen merkki ovat samat!")
elif valinta == "3":
    print("Merkkijono tulostettuna väärinpäin on '" + merkkijono[::-1] + "'.")
elif valinta == "0":
    print("Lopetetaan.")
else:
    print("Tuntematon valinta, lopetetaan.")

print("Kiitos ohjelman käytöstä.")
