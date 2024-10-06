print("Anna matkustajan ikä:")
ika = int(input())

lipun_hinta = 4.0  

if ika < 18 or ika >= 70:
    lipun_hinta *= 0.6
print(f"Lipun hinta on nyt {lipun_hinta:.2f} euroa.\n")

print("Onko matkustaja opiskelija? (k/e):")
opiskelija = input()
    
print("Onko matkustaja varusmies? (k/e):")
varusmies = input()
    
if opiskelija == 'k' or varusmies == 'k':
    lipun_hinta *= 0.7  
else:
    print(f"Lipun hinta on nyt {lipun_hinta:.2f} euroa.")

print(f"Lipun hinta on nyt {lipun_hinta:.2f} euroa.")

print("Matkustaako matkustaja ilta-alen aikaan? (k/e):")
ilta_ale = input()

if ilta_ale == 'k':
    lipun_hinta *= 0.8  # 20 % ilta-ale

print(f"Lipun lopullinen hinta valinnoillasi on {lipun_hinta:.2f} euroa.")
print("Kiitos ohjelman käytöstä.")
