# Määritellään Human-luokka luodaan 2 oliota halutuilla tiedoilla
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Nimi: {self.name}, Ikä: {self.age}'

# Luodaan kaksi oliota
name1 = Human("Adam", "18")
name2 = Human("Eva", "18")

