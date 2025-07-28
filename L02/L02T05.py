# Kysytään käyttäjältä hänen etunimi ja lasketaan kirjainten määrä sekä tulostetaan yhtä montakertaa alkukirjain
firstname = input("Anna etunimesi: ")
count_letters = len(firstname)
repeated_first_letter = firstname [0] * len(firstname)
print("Nimessäsi on "f"{count_letters} kirjanta.\n" f"{ repeated_first_letter}  ")