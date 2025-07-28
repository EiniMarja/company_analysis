# Tehdään ohjelma, joka laskee kokonaiskustannuksen annettujen rametrien (ajetut kilometrit, keskikulutus/100km, litrahinta) mukaan
def get_cost(distance, consumption_per_100km, price_per_litre):
    litres_used = (distance / 100) * consumption_per_100km
    cost = litres_used * price_per_litre
    return f"{cost:.2f} €"

def main():
    kilometers = None
    consumption = None
    price = None

    while True:
        try:
            if kilometers is None:
                kilometers = float(input("Anna ajetut kilometrit: "))
            if consumption is None:
                consumption = float(input("Anna keskikulutus (l/100 km): "))
            if price is None:
                price = float(input("Anna polttoaineen litrahinta (€): "))
            break  # Kaikki arvot on nyt annettu oikein
        except ValueError:
            print("\nVirheellinen syöte. Muista käyttää pistettä desimaalierottimena.")
            # Nollataan vain se arvo, joka aiheutti virheen
            if kilometers is not None and not isinstance(kilometers, float):
                kilometers = None
            if consumption is not None and not isinstance(consumption, float):
                consumption = None
            if price is not None and not isinstance(price, float):
                price = None

    result = get_cost(kilometers, consumption, price)

    # Tulostetaan taulukko
    header = f"{'Testi':<45}Tulos"
    row_modified = f"print(get_cost({int(kilometers)},{consumption:.1f},{price:.2f}))".ljust(45) + result
    line = "-" * len(row_modified)

    print(f"{header}\n{line}\n{row_modified}\n{line}")

if __name__ == "__main__":
    main()
