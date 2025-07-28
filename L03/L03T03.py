# Määritellään odotetut luvut jokaiselle kierrokselle
expected_values = [
    (10, 20),     # 1. kierros: hyväksytään 10 tai 20
    (100, 200),   # 2. kierros: hyväksytään 100 tai 200
    (55, )      # 3. kierros: hyväksytään vain 55
]

# Käydään läpi kolme kierrosta
for i in range(3):
    value = int(input("Anna luku: "))
    
    if value == expected_values[i][0] or value == expected_values[i][1]:
        print(f"Luku on {expected_values[i][0]} tai {expected_values[i][1]}")
    else:
        print(f"Luku on {value}")