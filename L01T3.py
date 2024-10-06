Luku1 = 234
Luku2 = 789

Summa = Luku1 + Luku2
Erotus = Luku2 - Luku1
Tulo = Luku1 * Erotus

Jakaja = 2
SummaJakojaannos = Summa % Jakaja
TuloJakojaannos = Tulo % Jakaja

print(Luku1, "+", Luku2, "=", Summa)
print(Luku2, "-", Luku1, "=", Erotus)
print(Luku1, "*", Erotus, "=", Tulo)
print(Luku1, "* (", Luku2, "-", Luku1, ") =", Tulo)
print("Summan", Summa, "jakojäännös luvulla", Jakaja, "on", SummaJakojaannos)
print("Tulon", Tulo, "jakojäännös luvulla", Jakaja, "on", TuloJakojaannos)
print("Kiitos ohjelman käytöstä.")
