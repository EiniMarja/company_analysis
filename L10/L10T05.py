#Tehdään ohjelma, joka kirjoittaa annetut sukunimet tiedostoon
def write_names_to_file(names: list[str], file_handler) -> None:
    filename = "sukunimet.txt"
    try:
        with file_handler(filename, "w", encoding="utf-8") as file:
            for name in names:
                file.write(name + "\n")
    except OSError as e:
        print(f"Virhe tiedostoon kirjoittamisessa: {e}")
#luetaan sukunimet avattuun tiedostoon ja palauttaa sen listana
def read_names_from_file(file_handler) -> list[str]:
    filename = "sukunimet.txt"
    try:
        with file_handler(filename, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print("Tiedostoa ei löytynyt.")
        return []
    except OSError as e:
        print(f"Virhe tiedoston lukemisessa: {e}")
        return []
#Kysytään käyttäjältä sukunimiä ja tallentaan ne
def process_names(input_func, output_func, file_write, file_read):
    names = []
    output_func("Syötä sukunimiä (tyhjä syöte lopettaa):")
    while True:
        name = input_func("Sukunimi: ").strip()
        if name == "":
            break
        names.append(name)
#Kirjoitetaan nimet tiedostoon
    write_names_to_file(names, file_write)
# Luetaan nimet tiedostosta ja tulostetaan ne
    output_func("\nTallennetut sukunimet tiedostosta:")
    read_names = read_names_from_file(file_read)
    for name in read_names:
        output_func(name)

def main():
    process_names(input, print, open, open)

if __name__ == "__main__":
    main()
