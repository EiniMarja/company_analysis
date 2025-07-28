# Tehdään ohjelma, joka laskeen kolmen kysytyn parametrin keskiarvon kahden desimaalin tarkkuudella
def average(a, b, c):
    return round((a + b + c) / 3, 2)
def main():
    try:
        parameter1 = int(input("Anna ensimmäinen parametri: "))
        parameter2 = int(input("Anna toinen parametri: "))
        parameter3 = int (input("Anna kolmas parametri: "))
        result = average(parameter1, parameter2, parameter3)
    
        # Muotoillaan testirivi ja tulosrivi 
        header = f"{'Testi':<25}Tulos"
        row_modified = f"print(average({parameter1},{parameter2},{parameter3}))".ljust(26) + str(result)
        line = "-" * len(row_modified)
        

        # Tulostetaan taulukko
        print(f"{header}\n{line}\n{row_modified}\n{line}")
    except ValueError:
        print("Virheellinen syöte! Syötä lukuarvo kahden desimaalin tarkkudella.")

if __name__ == "__main__":
    main()