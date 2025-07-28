# Pyydetään käyttäjää antamaan luku 1-10 väliltä
while True:
    try:
        number = int(input("Anna luku välillä 1–10: "))
        if 1 <= number <= 10:
            for i in range(1, number + 1):
                for j in range(1, number + 1):
                    result = i * j
                    print(f"{result:3} ", end="")
                print()
            break
        else:
            print("Virheellinen syöte.")
    except ValueError:
        print("Virheellinen syöte.")
    print() # Tehdään rivin vaihto, koska koodiin tulee muutoin jotain ylimäärästä merkkiä