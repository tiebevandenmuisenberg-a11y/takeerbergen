import random # Importeer de random module voor willekeurige keuzes

# Initialiseer scorevariabelen
wins = 0
loses = 0
gelijk = 0

opties = ["schaar", "steen", "papier"] # Mogelijke opties voor het spel

while True: # Oneindige lus voor het spel
    user = input("Kies Schaar, Steen of Papier (typ 'stop' om te stoppen): ").lower() # Vraag de gebruiker om een keuze
    if user == "stop":
        print("Spel gestopt!")
        print(f"Eindstand: Gewonnen: {wins}, Verloren: {loses}, Gelijk: {gelijk}") # Toon de eindstand
        break

    optie = random.choice(opties) # Willekeurige keuze voor de computer

    if user in opties:
        print(f"Jou optie: {user}\nMijn optie: {optie}") # Toon de keuzes
        
        if user == optie:
            print("Gelijkspel!")
            gelijk += 1

        # Bepaal de winnaar
        elif (user == "schaar" and optie == "papier") or \
             (user == "steen" and optie == "schaar") or \
             (user == "papier" and optie == "steen"):
            print("Je wint!")
            wins += 1
        
        else:
            print("Je bent verloren.")
            loses += 1

    else:
        print("Ongeldige keuze! Kies schaar, steen of papier.") # Foutmelding voor ongeldige invoer
