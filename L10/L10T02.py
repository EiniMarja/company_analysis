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
# Laskee nimien kokonaismäärän
def count_names(names: list[str]) -> int:
    return len(names)
# Laskee kuinka monta kertaa kukin nimi esiintyy
def count_name_occurrences(names: list[str]) -> dict[str, int]:
    occurrences = {}
    for name in names:
        occurrences[name] = occurrences.get(name, 0) + 1
    return occurrences
# Lajittelee nimet aakkosjärjestykseen
def sort_names(names: list[str]) -> list[str]:
    return sorted(names)

def print_name_statistics(total_count: int, name_occurrences: dict[str, int], sorted_names: list[str]) -> None:
    print(f"\nNimien kokonaismäärä: {total_count}")
    print("Nimien esiintymiskerrat aakkosjärjestyksessä:")
    for name in sorted_names:
        print(f"{name}: {name_occurrences.get(name, 0)}")

def main():
    file_path = "nimet.txt"
    try:
        names = read_names_from_file(file_path)
        total_count = count_names(names)
        name_occurrences = count_name_occurrences(names)
        sorted_names = sort_names(list(name_occurrences.keys()))
        print_name_statistics(total_count, name_occurrences, sorted_names)
    except Exception as e:
        print(f"Virhe: {e}")

if __name__ == "__main__":
    main()
