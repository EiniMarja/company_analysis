# Luodaan 4-luvun lista ja tehdään siihen muokkauksia ja tulostetaan alkuperäinen litsa ja muutokset
def create_list() -> list[int]:
    # Luodaan lista, jossa on neljä kokonaislukua
    return [10, 20, 30, 40]

def modify_element(numbers: list[int], index: int, new_value: int) -> bool:
    try:
        numbers[index] = new_value
        return True
    except IndexError:
        return False

def safe_print_element(numbers: list[int], index: int) -> None:
    try:
        print(f"Arvo listan indeksissä {index}: {numbers[index]}")
    except IndexError:
        print("indeksiä ei ole listassa")
def main():
    numbers = create_list()
    print(f"Alkuperäinen lista: {numbers}")

    # Yritetään muokata seuraavia elementtejä
    if modify_element(numbers, 2, 100):
        print(f"Muokattu lista: {numbers}")
    else:
        print("Elementin muokkaus epäonnistui.")

    # Yritetään muokata elementtiä, jota ei ole luodussa listassa
    if modify_element(numbers, 5, 500):
        print(f"Muokattu lista: {numbers}")
    else:
        print("Elementin muokkaus epäonnistui.")

    safe_print_element(numbers, 1)
    safe_print_element(numbers, 10)

if __name__ == "__main__":
    main()
