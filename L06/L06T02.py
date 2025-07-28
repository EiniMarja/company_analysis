# Tehdään ohjelma, joka muuntaan lämpötilan celsiuksesta  fahrenheitiin ja toisinpäin käyttäjän valinan mukaan
def celToFah(cel):
    # Muunnetaan Celsius-asteet Fahrenheitiksi
    fah = (cel * 9/5) + 32
    return round(fah, 1)

def fahToCel(fah):
    #Muunnetaan Fahrenheit-asteet Celsius-asteiksi
    cel = (fah - 32) * 5/9
    return round(cel, 1)

def main():
    while True:
        user_input = input("Anna lämpötila ja yksikkö: ")
        if user_input.lower() == "lopeta":
            break
        try:
            value, unit = user_input.strip().split()
            value = float(value)
            unit = unit.upper()
            if unit == "C":
                tulos = celToFah(value)
                testi = f"print(celToFah({value}))"
            elif unit == "F":
                tulos = fahToCel(value)
                testi = f"print(fahToCel({value}))"
            else:       
                continue

            header = f"{'Testi':<34}Tulos"
            row = f"{testi}".ljust(35) + str(tulos)
            line = "-" * len(row)

            print(f"{header}\n{line}\n{row}\n{line}\n")
            break  # Lopetetaan onnistuneen muunnoksen jälkeen

        except ValueError:
            print("Virheellinen syöte! Käytä muotoa 'arvo C' tai 'arvo F' antaessasi lämpötilan")

    print("Ohjelma lopetettu.")

if __name__ == "__main__":
    main()
