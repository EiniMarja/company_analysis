# Alustetaan summa
summa = 0

# Kysytään käyttäjältä viisi lukua ja lasketaan positiivisten lukujen summa
for i in range(5):
    value = int(input(f"Anna {i+1}. luku: "))
    if value > 0:
        summa += value

print(f"Lukujen summa on: {summa}")