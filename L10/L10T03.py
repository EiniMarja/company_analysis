#Tehdään ohjelma, joka kysyy käyttäjältä lukuja ja tallentaa kokonaisluvut ja liukuluvut eri tiedostoihin.
# Kysytään käyttäjältä syöte 
def get_number_input() -> str:
    try:
        return input("Anna luku tai tyhjä -lopettaa ohjelman: ").strip()
    except EOFError:
        return ""
# Tarkistetaan, onko syöte kokonaisluku tai liukuluku
def classify_number(input_str: str) -> str:
    if input_str == "":
        return "error"
    try:
        int(input_str)
        return "int"
    except ValueError:
        try:
            float(input_str)
            return "float"
        except ValueError:
            return "error"
# Kirjoitetaan luku/luvut tiedostoon
def write_to_file(number: str, file_path: str) -> None:
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(number + "\n")
    except OSError as e:
        print(f"Virhe tiedostoon kirjoittamisessa ({file_path}): {e}")


def process_numbers() -> tuple[int, int]:
    int_count = 0
    float_count = 0
    int_file = "kokonaisluvut.txt"
    float_file = "liukuluvut.txt"

    while True:
        user_input = get_number_input()
        if user_input == "":
            print("Tyhjä syöte. Lopetetaan.")
            break

        classification = classify_number(user_input)

        if classification == "int":
            write_to_file(user_input, int_file)
            int_count += 1
        elif classification == "float":
            write_to_file(user_input, float_file)
            float_count += 1
        else:
            print("Virheellinen syöte. Lopetetaan.")
            break
    return (int_count, float_count)
def main():
    int_file = "kokonaisluvut.txt"
    float_file = "liukuluvut.txt"
    int_count, float_count = process_numbers()
    print(f"\nTallennettu {int_count} kokonaislukua tiedostoon {int_file}")
    print(f"Tallennettu {float_count} liukulukua tiedostoon {float_file}")
    print("Tarkista tiedostojen sisältö tekstieditorilla.")


if __name__ == "__main__":
    main()
