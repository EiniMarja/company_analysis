# Tehdään Ohjelma, joka pyytää oppilaiden nimet ja laittaa ne aakkosjärjestykseen sekä laskee nimienlukumäärän
import re  # Tuodaan moduuli, jolla varmistetaan että sallitaan vain tekstiä
def get_student_names():
    names = []
    while True:
        name = input("Enter student name: ").strip()
        if name == "":
            break
        # Sallitaan vain kirjaimet (myös ä, ö, å) ja mahdollinen välilyönti
        if not re.fullmatch(r"[A-Za-zÄÖÅäöå\s]+", name):
            print("Invalid name. Please use letters only (no numbers or symbols).")
            continue
        # Estetään duplikaatit (verrataan pieniksi kirjaimiksi muunnettuna)
        if name.lower() in [n.lower() for n in names]:
            print("This name has already been added.")
            continue
        names.append(name)
    return ",".join(sorted(names))

def count_students(name_string):
    if name_string == "":
        return 0
    return name_string.count(",") + 1

def main():
    student_names_string = get_student_names()
    number_of_students = count_students(student_names_string)
    
    print(f"Student count: {number_of_students}")
    print(student_names_string)

if __name__ == "__main__":
    main()
