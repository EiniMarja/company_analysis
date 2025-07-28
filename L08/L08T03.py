# Tehdään ohjelma, joka laskee arvosanojen (0-5) määrän ja keskiarvon
def input_grade() -> int | None:
    while True:
        grade = input("Syötä kurssiarvosana väliltä (0–5), tyhjä lopettaa ohjelman: ")
        if grade == "":
            return None
        try:
            value = int(grade)
            if 0 <= value <= 5:
                return value
            else:
                print("Arvosanan tulee olla väliltä (0–5).")
        except ValueError:
            print("Virheellinen syöte. Anna kokonaisluku väliltä (0–5) tai paina Enter lopettaaksesi.")

def collect_grades() -> list[int]:
    grades = []
    while True:
        grade = input_grade()
        if grade is None:
            break
        grades.append(grade)
    return grades

def calculate_average(grades: list[int]) -> float:
    if not grades:
        return 0.0
    return sum(grades) / len(grades)

def display_results(grades: list[int]) -> None:
    print(f"\nArvosanoja yhteensä: {len(grades)}")
    average = calculate_average(grades)
    print(f"Keskiarvo: {average:.1f}")

def main():
    grades = collect_grades()
    display_results(grades)

if __name__ == "__main__":
    main()
