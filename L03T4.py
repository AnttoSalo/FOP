print("Selvitetään opiskelijan kurssiarvosana pisteiden perusteella.")

pisteet = int(input("Anna opiskelijan pisteet: "))

print("Selvitetäänkö arvosana")
print("1) yhdellä monihaaraisella valintarakenteella")
print("2) useilla erillisillä valintarakenteilla")

valinta = int(input("Anna valintasi: "))

if valinta == 1:
    if pisteet >= 90:
        arvosana = 5
    elif pisteet >= 80:
        arvosana = 4
    elif pisteet >= 70:
        arvosana = 3
    elif pisteet >= 60:
        arvosana = 2
    elif pisteet >= 50:
        arvosana = 1
    else:
        arvosana = 0
    print(f"Annoit pisteiksi {pisteet}/100.")
    print(f"Kurssin arvosana on tällöin {arvosana}.")
    
#Tämähän on nyt tehty väärin, mutta en ymmärrä miten teen ohjelman siten, että se antaa vääriä tulosteita... 
elif valinta == 2:
    arvosana = 0
    if pisteet >= 50:
        arvosana = 1
    if pisteet >= 60:
        arvosana = 2
    if pisteet >= 70:
        arvosana = 3
    if pisteet <= 80:
        arvosana = 4
    else:
        if pisteet >= 90:
            arvosana = 5
    print(f"Annoit pisteiksi {pisteet}/100.")
    print(f"Kurssin arvosana on tällöin {arvosana}.")
    
else:
    print("Tuntematon valinta.")

print("Kiitos ohjelman käytöstä.")
