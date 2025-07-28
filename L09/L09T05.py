#Tehdään ohjelma ,joka käsittelee merkkijonon poikkeustilanteita
class InvalidIndexError(Exception):
    pass

class EmptyStringError(Exception):
    pass

def validate_index(index: int, max_index: int) -> None:
    if not (0 <= index <= max_index):
        raise InvalidIndexError(f"Indeksi {index} ei ole välillä 0 - {max_index}.")
    pass
def validate_string(s: str) -> None:
    if not s.strip():
        raise EmptyStringError("Merkkijono ei saa olla tyhjä.")
pass
def insert_string_with_validation(strings: list[str], index: int, new_string: str) -> list[str]:
    validate_index(index, len(strings))
    validate_string(new_string)
    strings.insert(index, new_string)
    return strings

def main():
    strings = ["a", "b", "c", "d", "e"]
    print("Alkuperäinen lista:")
    print(strings)

    try:
        updated_strings = insert_string_with_validation(strings, 2, "f")
        print("Päivitetty lista:")
        print(updated_strings)
    except (InvalidIndexError, EmptyStringError) as e:
        print(f"Virhe: {e}")

    try:
        updated_strings = insert_string_with_validation(strings, 10, "g")
    except (InvalidIndexError, EmptyStringError) as e:
        print(f"Virhe: {e}")

    try:
        updated_strings = insert_string_with_validation(strings, 1, "")
    except (InvalidIndexError, EmptyStringError) as e:
        print(f"Virhe: {e}")

if __name__ == "__main__":
    main()
