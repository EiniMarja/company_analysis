# Tehdään ohjelma, joka muuntaa käyttäjän antaman sekunttimäärän muotoon tunnit:minuutit:sekunnit
def showtime(sec):
    hours = sec // 3600
    minutes = (sec % 3600) // 60
    seconds = sec % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def main():
    ohjelma_kaynnissa = True
    while ohjelma_kaynnissa:
        user_input = input("Anna aika sekunteina: ")
        if user_input.lower() == "lopeta":
            break
        try:
            sec = int(user_input.strip())
            if sec < 0:
                print("Syötteen täytyy olla positiivinen kokonaisluku.")
                continue
            tulos = showtime(sec)
            header = f"{'Testi':<45}Tulos"
            row = f"print(showtime({sec}))".ljust(45) + tulos
            line = "-" * len(row)

            print(f"{header}\n{line}\n{row}\n{line}\n")

            break  # Lopetetaan ohjelma onnistuneen tuloksen jälkeen

        except ValueError:
            print("Virheellinen syöte! Syötä positiivinen kokonaisluku tai 'lopeta'.\n")

    print("Ohjelma lopetettu.")  #Tulostetaan "ohjelma lopetettu", kun on saatu käyttäjältä kelpaava syöte

if __name__ == "__main__":
    main()
