# Tulostetaan koe arvosana käyttäjältä kysytyn pistemäärän mukaissti
scores = int(input("Anna pistemäärä: "))
# Tarkista pisteväli ja tulostetaan arvosana
if 0 <= scores <= 1:
    print("Arvosana: 0")
elif 2 <= scores <= 3:
    print("Arvosana: 1")
elif 4 <= scores <= 5:
    print("Arvosana: 2")
elif 6 <= scores <= 7:
    print("Arvosana: 3")
elif 8 <= scores <= 9: 
    print("Arvosana: 4")
elif 10 <= scores <= 12:
    print("Arvosana: 5")
else:
    print("Pistemäärä ei ole salittu. Anna pistemäärä väliltä 0-12.")
