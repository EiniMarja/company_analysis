# Tehdään ohjelma. joka muuttaa tuumamitan senttimetreiksi
def inches_to_cm(inches):
    return inches * 2.54 #muutetaan tuumamitta senttimetreksi 1 ich = 2.54 cm

def format_output(inches, cm):
    return f"{inches} tuumaa on {round(cm, 2)} cm"

def main():
    while True:
        user_input = input("Anna tuumamäärä (0 lopettaa ohjelma): ")
        try:
            inches = float(user_input)
            if inches == 0:
                print("Syötit nollan. Ohjelma lopetetaan 👋")
                break
            cm = inches_to_cm(inches)
            print(format_output(inches, cm))
        except ValueError:
            print("❌ Virheellinen syöte. Syötä lukuarvo tuumina.")

if __name__ == "__main__":
    main()
