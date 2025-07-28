# Tehdään ohjelma, joka tulostaa testin ja tuloksen 
def show_info():
    test= "print(show_info())"
    result = "Olen Info-funktio"
    header = f"{'Testi':<20}Tulos"
    row_modified = f"{test:<20}{result}"
    line = "-" * len(row_modified)
    return f"{header}\n{line}\n{row_modified}\n{line}"

def main():
    # Tulostetaan taulukko
    print(show_info())

if __name__ == "__main__":
    main()