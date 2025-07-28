# Kysytään käyttäjältä sademäärä 7 kertaa (viikonajalta) ja lasketaan sademäärien summa
total_rainfall = 0 #Alustetaan laskuri

for i in range(7):
            rain_per_day = int(input(f"Anna sademäärä: "))
            if rain_per_day >= 0:
                total_rainfall += rain_per_day
            else:
                pass
# Tulostetaan kokonaissademäärä
print(f"Sademäärä yhteensä: {total_rainfall}")