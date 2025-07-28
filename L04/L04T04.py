# Kysytään käyttäjältä etu- ja sukunimi ja tulostetaan etunimen kirjainta etuminen pituuden verran ja tulostetaan sukunumi oikealta vasemalle
first_name = input("Anna etunimi: ")
last_name = input("Anna sukunimi: ")
# Etunimen ensimmäistä kirjaimen toitsaminen
first_letter= first_name[0]
repeated_letter = len(first_name)
for i in range(repeated_letter):
    print(first_letter, end="")
print()  #Tehdään rivin vaihto, jotta saadaan tulostukset siistimmim näkyviin
# Tulostetaan sukunimi oikealta vasemmalle
for i in range(len(last_name) - 1, -1, -1):
    print(last_name[i], end="")
print()  #Tehdään rivin vaihto, koska koodiin tulee muutoin jotain ylimäärästä merkkiä