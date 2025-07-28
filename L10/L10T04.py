#Tehdään ohjelma, joka arpoo lottonumeroita
import random
#Arp7 lottonumero välillä 1-40 ja palautta ne
def generate_lottery_numbers() -> list[int]:
    return sorted(random.sample(range(1, 41), 7))
# Muuntaa listan numeroita merkkijonoksi
def format_lottery_numbers(numbers: list[int]) -> str:
    return " ".join(str(n) for n in numbers)
# Tallentaa annetun merkkijonon tiedostoon
def save_lottery_numbers(numbers: str, file_path: str) -> None:
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(numbers + "\n")
#Suorittaa lottoarvonnan
def run_lottery() -> list[int]:
    """Suorittaa lottoarvonnan ja tallentaa tuloksen tiedostoon."""
    numbers = generate_lottery_numbers()
    formatted = format_lottery_numbers(numbers)
    save_lottery_numbers(formatted, "lotto.txt")
    return numbers

def main():
    file_path = "lotto.txt"
    try:
        lottery_numbers = run_lottery()
        print(f"Arvotut lottonumerot: {format_lottery_numbers(lottery_numbers)}")
        print(f"Numerot on tallennettu tiedostoon {file_path}")
    except Exception as e:
        print(f"Virhe: {e}")

if __name__ == "__main__":
    main()
