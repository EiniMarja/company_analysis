# Kerätään käyttäjän antamat rekisterinumerot ja näytetään aakkosjärjestyksessä ne käyttäjälle
def collect_registration_numbers():
    numbers = []
    print("Anna rekisterinumeroita (tyhjä syöte lopettaa ohjelman):")
    while True:
        num = input("> ")
        if num == "":
            break
        if len(num) > 7:
            print("Liian pitkä rekisterinumero (max.7 merkkiä)")
            continue
        numbers.append(num)
    return numbers

def sort_registration_numbers(numbers):
    return sorted(numbers)

def display_sorted_numbers(sorted_numbers):
    print("\nJärjestetyt rekisterinumerot:")
    for num in sorted_numbers:
        print(num)

def main():
    numbers = collect_registration_numbers()
    sorted_numbers = sort_registration_numbers(numbers)
    display_sorted_numbers(sorted_numbers)

if __name__ == "__main__":
    main()
