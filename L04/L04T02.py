# Kysytään käyttäjältä kokonslukua, niin kauan kunnes käyttäjä ei anna mitään syötettä, jonka jälkeen 
count = 0 # Alustetaan lukumäärä 
summa = 0
while True:
    user_input = input(f"Anna luku: ")
    
    if user_input == "":
        break  # Jos käyttjä antaa Tyhjä syöten → lopetetaan ohjelma
    
    else:
        number = int(user_input)
        count += 1
        summa += number
# Tulostetaan annettujen lukujen lukumää ja summa
print(f"Lukuja annettu: {count}")
print(f"Lukujen summa: {summa}")