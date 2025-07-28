# Tehdään ohjelma, jossa 1. pyydetystä parametrista vähennetään 2. pyydetty parametri
def subtract(a, b):
    return a - b

def main():
    try:
        parameter1 = int(input("Anna ensimmäinen parametri: "))
        parameter2 = int(input("Anna toinen parametri: "))
        difference = subtract(parameter1, parameter2)

        # Muotoillaan testirivi ja tulosrivi 
        header = f"{'Testi':<25}Tulos"
        row_modified = f"print(subtract({parameter1},{parameter2}))".ljust(28) + str(difference)
        line = "-" * len(row_modified)

        # Tulostetaan taulukko
        print(f"{header}\n{line}\n{row_modified}\n{line}")
    except ValueError:
        print("Virheellinen syöte! Syötä lukuarvo.")

if __name__ == "__main__":
    main()