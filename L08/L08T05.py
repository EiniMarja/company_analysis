# Auton rekisterin luonti ja riskisteriin lisättyjen autojen tietojen esittäminen 2 eri tavalla aakkosjärjstyksessä
def create_registry() -> dict[str, dict[str, str | int]]:
    return {}

# Luo auton tiedot sanakirjana
def create_car(reg_number: str, brand: str, model: str, year: int) -> dict[str, dict[str, str | int]]:
    return {
        reg_number: {
            "brand": brand,
            "model": model,
            "year": year
        }
    }
def add_car(registry: dict[str, dict[str, str | int]], car: dict[str, dict[str, str | int]]) -> None:
    registry.update(car)

# Tulostaa autojen tiedot aakkosjärjestyksessä automerkin mukaan
def print_by_brand(registry: dict[str, dict[str, str | int]]) -> None:
    sorted_items = sorted(registry.items(), key=lambda item: item[1]['brand'])
    for reg_number, info in sorted_items:
        print(f"{reg_number}: {info['brand']} {info['model']} {info['year']}")
# Tulostetaan autonrekisterinumerin mukaan aakkosjärjestykseen
def print_by_reg_number(registry: dict[str, dict[str, str | int]]) -> None:
    for reg_number in sorted(registry.keys()):
        info = registry[reg_number]
        print(f"{reg_number}: {info['brand']} {info['model']} {info['year']}")


def main():
    registry = create_registry()
    cars = [
        create_car("ABC-123", "Skoda", "Octavia", 2020),
        create_car("XYZ-789", "Toyota", "Corolla", 2019),
        create_car("DEF-456", "Volvo", "V60", 2021),
        create_car("GHI-789", "Ford", "Focus", 2018),
        create_car("JKL-012", "Honda", "Civic", 2022)
    ]
    for car in cars:
        add_car(registry, car)

    print("Autot merkin mukaan:")
    print_by_brand(registry)

    print("\nAutot rekisterinumeron mukaan:")
    print_by_reg_number(registry)
   
if __name__ == "__main__":
    main()
