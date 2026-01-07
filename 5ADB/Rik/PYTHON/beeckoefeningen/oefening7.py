import random # Importeer de random module om willekeurige getallen te genereren

# Genereer drie willekeurige worpen van een zeszijdige dobbelsteen
a = random.randint(1, 6)
b = random.randint(1, 6)
c = random.randint(1, 6)

print("Worpen:", a, b, c) # Print de drie worpen

if a == b == c: # Controleer of alle drie de worpen gelijk zijn
    print("De drie worpen zijn gelijk.")

elif a == b or a == c or b == c: # Controleer of er twee worpen gelijk zijn
    print("Er zijn er twee worpen gelijk.")

else: # Als geen van de bovenstaande voorwaarden waar is, zijn alle worpen verschillend
    print("Alle worpen zijn verschillend.")

worpen = sorted([a, b, c]) # Sorteer de worpen om de opeenvolging te controleren
if worpen[2] - worpen[1] == 1 and worpen[1] - worpen[0] == 1: # Controleer of de worpen een opeenvolging vormen
    print("De worpen volgen een opeenvolging.") # Print dat de worpen een opeenvolging vormen