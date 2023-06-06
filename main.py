numer_pesel = input("Podaj swój numer pesel:")
if len(numer_pesel) != 11:
    print("Zły numer pesel")

rok_urodzenia = numer_pesel[0:2]
rok_urodzenia = int(rok_urodzenia)



miesiac_urodzenia = numer_pesel[2:4]
miesiac_urodzenia = int(miesiac_urodzenia)


dzien_urodzenia = numer_pesel[4:6]


okreslenie_płci = numer_pesel[6:10]
okreslenie_płci = int(okreslenie_płci)


print("WSZYSTKIE DANE O TOBIE WYCZYTANE Z NUMERU PESEL:")
if rok_urodzenia <= 99 and rok_urodzenia >= 24:
    print(f"Twój rok urodzenia to 19{rok_urodzenia}")
else:
    rok_urodzenia = str(rok_urodzenia)
    print(f"Twój rok urodzenia to 20{rok_urodzenia}")

if miesiac_urodzenia >= 21:
    if miesiac_urodzenia == 21:
        print(f"Twoja data urodzin to {dzien_urodzenia}.01")
    elif miesiac_urodzenia == 22:
        print(f"Twoja data urodzin to {dzien_urodzenia}.02")
    elif miesiac_urodzenia == 23:
        print(f"Twoja data urodzin to {dzien_urodzenia}.03")
    elif miesiac_urodzenia == 24:
        print(f"Twoja data urodzin to {dzien_urodzenia}.04")
    elif miesiac_urodzenia == 25:
        print(f"Twoja data urodzin to {dzien_urodzenia}.05")
    elif miesiac_urodzenia == 26:
        print(f"Twoja data urodzin to {dzien_urodzenia}.06")
    elif miesiac_urodzenia == 27:
        print(f"Twoja data urodzin to {dzien_urodzenia}.07")
    elif miesiac_urodzenia == 28:
        print(f"Twoja data urodzin to {dzien_urodzenia}.08")
    elif miesiac_urodzenia == 29:
        print(f"Twoja data urodzin to {dzien_urodzenia}.09")
    elif miesiac_urodzenia == 30:
        print(f"Twoja data urodzin to {dzien_urodzenia}.10")
    elif miesiac_urodzenia == 31:
        print(f"Twoja data urodzin to {dzien_urodzenia}.11")
    elif miesiac_urodzenia == 32:
        print(f"Twoja data urodzin to {dzien_urodzenia}.12")
else:
        print(f"Twoja data urodzin to {dzien_urodzenia}.{miesiac_urodzenia}")

 

if okreslenie_płci % 2 == 0:
    print("Jesteś kobietą")
else:
    print("Jesteś facetem")
