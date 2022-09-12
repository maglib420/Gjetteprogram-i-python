from random import randint, random

spillPaaNytt = True


while spillPaaNytt == True:
    forsøk = 1
    nummer = randint(1,10)

    gjett = int(input("Gjett et tall mellom 1 og 10."))

    while gjett != nummer:
        if gjett < nummer:
            print("Du gjettet for lavt.")
            gjett = int(input("Gjett igjen."))
            forsøk = forsøk + 1
        elif gjett > nummer:
            print("Du gjettet for høyt.")
            gjett = int(input("Gjett igjen."))
            forsøk = forsøk + 1

    print()
    print("Du gjettet riktig nummer!")
    print("Det tok deg bare", forsøk, "forsøk :)")
    print()
    spillPaaNyttSvar = input("Vil du spille igjen? Svar 'Ja eller Nei")

    print(spillPaaNytt)

    if spillPaaNyttSvar == "Nei":
        spillPaaNytt = False

