#Tehdään ohjelma, jolla käsitellään merkkijonoa
from typing import Any

def initialize_list() -> list[str]:
    return ["Toyota", "BMW", "Ford", "Tesla", "Volkswagen"]

def get_valid_index(max_index: int) -> int:
    while True:
        try:
            index = int(input(f"Anna indeksi (0 - {max_index}): "))
            if 0 <= index <= max_index:
                return index
            else:
                print("Indeksi ei ole sallitulla välillä. Yritä uudelleen.")
        except ValueError:
            print("Virheellinen syöte. Anna kokonaisluku.")

def get_valid_string() -> str:
    while True:
        user_input = input("Anna uusi merkkijono: ").strip()
        if user_input:
            return user_input
        else:
            print("Syöte ei saa olla tyhjä. Yritä uudelleen.")

def insert_string(strings: list[str], index: int, new_string: str) -> list[str]:
    strings.insert(index, new_string)
    return strings

def print_list(strings: list[str]) -> None:
    print(", ".join(strings))

def main():
    strings = initialize_list()
    print("Alkuperäinen lista:")
    print_list(strings)

    max_index = len(strings)  # sallitaan myös lisäys listan loppuun
    index = get_valid_index(max_index)
    new_string = get_valid_string()

    updated_strings = insert_string(strings, index, new_string)
    print("Päivitetty lista:")
    print_list(updated_strings)

if __name__ == "__main__":
    main()
