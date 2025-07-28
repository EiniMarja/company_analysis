# Määritellään Mobile -luokka ja luodaan 2 oliota sekä tulostetaan niiden tiedot
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __repr__(self):
        return f'Mobile("{self.brand}", "{self.model}", {self.price})'

# Luodaan kaksi oliota
phone1 = Mobile("Samsung", "Galaxy", 349)
phone2 = Mobile("Apple", "iPhone 12", 899)

# Tulostetaan oliot
print(f"Phone1 = {phone1}\nPhone2 = {phone2}")


