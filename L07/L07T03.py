# Määritellään Cat-luokka ja tulostetaan titoja sekä naukuminen
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def __str__(self):
        return f"{self.name}, Color: {self.color}"
    
    def miau(self):
        print("Meoooooow!")  

# Luodaan kaksi Cat-oliota
cat1 = Cat("Kit", "black")
cat2 = Cat("Kat", "white")

# Tulostetaan ominaisuudet
print(cat1)  # Kit, Color: black
print(cat2)  # Kat, Color: white

# Tulostetaan kissa1 naukumaan
cat1.miau()  

