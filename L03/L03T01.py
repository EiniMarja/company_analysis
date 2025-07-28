# Tuodaan random (module)
import random
# Kysytään käyttäjältä kaksi kokonaislukua
integer1 = int(input("Anna kokonaisluku: "))
integer2 = int(input("Anna kokonaisluku: "))
# Haetaan pienin luku ja tulostetaan se
if integer1 < integer2:
    print(integer1)
elif integer2 < integer1:
    print(integer2)
else:
    chosen_int = random.choice([integer1, integer2])
    print(f"{chosen_int}")

