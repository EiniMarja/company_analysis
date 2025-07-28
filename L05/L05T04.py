# Tehdään ohjelma, joka laskee kokonaiskulutuksen annettujen parametrien (ajetut kilometrit, keskikulutus/100km) mukaan
def get_fuel(distance, consumption_per_100km):
    litres_used = (distance / 100) * consumption_per_100km
    return f"{litres_used:.1f} ltr"

def main():
    kilometers = None
    consumption = None

    while True:
        try:
            if kilometers is None:
                kilometers = float(input("Anna ajetut kilometrit: "))
            if consumption is None:
                consumption = float(input("Anna keskikulutus (l/100 km): "))
            break  # Kaikki arvot on nyt annettu oikein
        except ValueError:
            print("\nVirheellinen syöte. Muista käyttää pistettä desimaalierottimena.")
            # Nollataan vain se arvo, joka aiheutti virheen
            if kilometers is not None and not isinstance(kilometers, float):
                kilometers = None
            if consumption is not None and not isinstance(consumption, float):
                consumption = None

    result = get_fuel(kilometers, consumption)

    # Tulostetaan taulukko
    header = f"{'Testi':<45}Tulos"
    row_modified = f"print(get_fuel({int(kilometers)},{consumption:.1f}))".ljust(45) + result
    line = "-" * len(row_modified)

    print(f"{header}\n{line}\n{row_modified}\n{line}")

if __name__ == "__main__":
    main()
