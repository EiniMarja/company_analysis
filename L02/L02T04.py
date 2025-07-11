#Tuodaan Pythoniin datetime (class)
from datetime import datetime
#Kysytään käyttäjältä hänen etunimi ja syntymävuosi3
firstname = input("Anna etunimesi: ")
birth_year= int(input("Anna syntymävuotesi: "))
recent_year = datetime.now().year
age = recent_year - birth_year
print ("Etunimesi:" f"{firstname}\n Syntymävuotesi:"f"{birth_year}\n Hei," f"{firstname}, olet "f"{age} vuotta vanha.")