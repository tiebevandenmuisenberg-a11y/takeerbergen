jaar = int(input("Geef het jaar dat je wilt controleren of het een schrikkeljaar is: ")) # Vraag het jaar aan de gebruiker
if (int(jaar) % 4 == 0 and int(jaar) % 100 != 0): # Controleer of het jaar deelbaar is door 4 maar niet door 100
    if (int(jaar) % 400 != 0):
        print (f"{jaar} is een schrikkeljaar.")# Print als het een schrikkeljaar is
else:
    print (f"{jaar} is geen schrikkeljaar.") # Print als het geen schrikkeljaar is