import random
# Kysytään käyttäjältä kolme kokonaislukua
integer1 = int(input("Anna kokonaisluku: "))
integer2 = int(input("Anna kokonaisluku: "))
integer3 = int(input("Anna kokonaisluku: "))
# Haetaan pienin luku ja tulostetaan se 
if integer1 >= integer2  and  integer1 >= integer3:
    biggest = integer1
elif integer2 >= integer1 and integer2 >= integer3:
    biggest = integer2
else:
    biggest = integer3
print(biggest)
