#Tehdään ohjelma, joka käsittelee tiedostossa olevia nimiä
def read_names_from_file(file_path: str) -> list[str]:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            names = [line.strip() for line in file if line.strip()]
        return names
    except FileNotFoundError:
        raise FileNotFoundError(f"Tiedostoa '{file_path}' ei löytynyt.")
    except IOError as e:
        raise IOError(f"Tiedoston käsittelyssä tapahtui virhe: {e}")
#Lasketaan ja palauttaa nimien kokonaismäärä
def count_names(names: list[str]) -> int:
    return len(names)
#Lasketaan kunkin nimen esiintymiskerrat ja palautetaan sanakirjana
def count_name_occurrences(names: list[str]) -> dict[str, int]:
    occurrences = {}
    for name in names:
        occurrences[name] = occurrences.get(name, 0) + 1
    return occurrences

def print_name_statistics(total_count: int, name_occurrences: dict[str, int]) -> None:
    print(f"\nNimien kokonaismäärä: {total_count}")
    for name in sorted(name_occurrences):
        print(f"{name}: {name_occurrences[name]}")

def main():
    file_path = "nimet.txt" 
    try:
        names = read_names_from_file(file_path)
        total_count = count_names(names)
        name_occurrences = count_name_occurrences(names)
        print_name_statistics(total_count, name_occurrences)
    except Exception as e:
        print(f"Virhe: {e}")

if __name__ == "__main__":
    main()
