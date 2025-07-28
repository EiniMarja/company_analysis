# Kysytään käyttäjältä hänen kokonimeänsä
fullname = input("nimi = ")
i = fullname.find(' ')
# Slice-syntaksilla haetaan etunimen ja sukunimen erottelu 
firstname = fullname[:i]
lastname = fullname[i+1:]
last_index = len(fullname) 
print(f"{firstname}\nnimi[0:{i}]\n{lastname}\nnimi[{i+1}:{last_index}]")