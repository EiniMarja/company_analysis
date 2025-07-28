# Kysytään käyttäjältä kokonaisluku 1-10 völiltä niin kauan, että käyttäjä antaa kokonailuvun halutulta väliltä
while True:
    try:
        number = int(input("Anna luku väliltä 1–10: "))
        if 1 <= number <= 10:
            break  # Poistutaan silmukasta kun kelvollinen luku on annettu
        else:
            print("Luvun täytyy olla välillä 1–10. Yritä uudelleen.")
    except ValueError:
        print("Luvun täytyy olla kokonaisluku. Yritä uudelleen.")
# Tulostetaan luvut yhdesä annettuun lukuun sekä niiden neliöt
for i in range(1, number + 1):
    print(f"Luvun {i} neliö on {i**2}")