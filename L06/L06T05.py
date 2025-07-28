def calculate_discount(quantity):
    if 10 <= quantity <= 49:
        return 5
    elif 50 <= quantity <= 99:
        return 10
    elif quantity >= 100:
        return 15
    else:
        return 0

def calculate_final_price(price, quantity, discount_percentage):
    discount = (discount_percentage / 100) * price * quantity
    final_price = (price * quantity) - discount
    return round(final_price, 2)

def get_valid_price():
    while True:
        try:
            price = float(input("Syötä tuotteen hinta: "))
            if price > 0:
                return price
            print("❌ Hinnan on oltava positiivinen lukuarvo.\n")
        except ValueError:
            print("❌ Virheellinen syöte. Syötä postiivinen lukuarvo.\n")

def get_valid_quantity():
    while True:
        try:
            quantity = int(input("Syötä ostettava määrä: "))
            if quantity > 0:
                return quantity
            print("❌ Määrän on oltava positiivinen kokonaisluku.\n")
        except ValueError:
            print("❌ Virheellinen syöte. Syötä postiivinen kokonaisluku.\n")

def main():
    while True:
        # Hinta ja määrä pyydetään erikseen, mutta virhe ei palauta koko ohjelmaa alkupisteeseen
        price = get_valid_price()
        quantity = get_valid_quantity()

        discount = calculate_discount(quantity)
        final_price = calculate_final_price(price, quantity, discount)

        print(f"Alennusprosentti: {discount}%")
        print(f"Lopullinen hinta: {final_price} euroa")

if __name__ == "__main__":
    main()
