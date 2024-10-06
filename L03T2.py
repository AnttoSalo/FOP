print("Selvitetään onko sana palindromi.")
sana = input("Anna sana, jonka ominaisuuksia tarkastellaan: ")
if sana == sana[::-1]:
    print("Sana '" + sana + "' on palindromi.")
else:
    print("Sana '" + sana + "' ei ole palindromi. Se on väärinpäin '" + sana[::-1] + "'.")

print("\nSelvitetään merkin sisältyminen merkkijonoon.")
kirjain = input("Anna kirjain: ")
if kirjain in sana:
    print("Kirjain '" + kirjain + "' löytyy sanasta '" + sana + "'.")
else:
    print("Kirjain '" + kirjain + "' ei löydy sanasta '" + sana + "'.")

eka_kirjain = sana[0]
vika_kirjain = sana[-1]

print("\nTässä tarkistetaan sanan ensimmäisen ja viimeisen kirjaimen erot.")
if eka_kirjain == vika_kirjain:
    print("Sanan '" + sana + "' ensimmäinen ja viimeinen kirjain ovat samat.")
else:
    if eka_kirjain < vika_kirjain:
        print("Sanan ensimmäinen kirjain on aakkosissa ennen sanan viimeistä kirjainta.")
    else:
        print("Sanan viimeinen kirjain on aakkosissa ennen sanan ensimmäistä kirjainta.")

print("\nKiitos ohjelman käytöstä.")
