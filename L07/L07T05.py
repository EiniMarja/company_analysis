# Määritellään Car-luokka ja tulostetaan autojen tiedot
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} {self.price}"

# Luodaan kolme Car-oliota
car1 = Car("Skoda", "Octavia", 3000)
car2 = Car("Audi", "A4", 4000)
car3 = Car("Volvo", "V70", 5000)

# Tulostetaan autojen tiedot
print(f"car1: {car1}")
print(f"car2: {car2}")
print(f"car3: {car3}")

# Lasketaan autojen yhteishinta
total_price = car1.price + car2.price + car3.price
print(f"Total price of the cars is {total_price}")
