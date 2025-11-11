import random

dict_pok = {
    "Pikachu": 40,
    "Dracaufeu": 180,
    "Carapuce": 60,
    "Bulbizarre": 55,
    "Salamèche": 70,
    "Rondoudou": 35,
    "Evoli": 50,
    "Mewtwo": 300,
    "Mew": 250,
    "Ronflex": 160,
    "Goupix": 45,
    "Psykokwak": 65,
    "Magicarpe": 10,
    "Lokhlass": 120,
    "Tortank": 200,
    "Florizarre": 190,
    "Dracolosse": 220,
    "Alakazam": 150,
    "Arcanin": 170,
    "Noctali": 130
}

responses_found = [
    "💥 {name} frappe avec {power} points!",
    "💥 Boom! {name} explose l'arène avec {power} points!",
    "💥 {name} frappe avec {power} points!",
    "💥 Boom! {name} explose l'arène avec {power} points!",
    "😵 {name} est confus et ne parvient pas à attaquer..."
]
responses_not_found = [
    "🤔 Ce Pokémon ne doit pas être dans ton Pokédex...",
    "😵 Aucun signal de ce Pokémon..."
]

i=1
print("🎮 Bienvenue dans le Pokédex interactif ! Tape 'exit' pour quitter.")

while True:
    given_key = input(f"\nTour {i} - Entre un nom de Pokémon: ").capitalize()
    if given_key.lower() == "exit":
        print("👋 À bientôt, dresseur Pokémon !")
        break
    found = False
    for key, value in dict_pok.items():
        if given_key == key:
            print(random.choice(responses_found).format(name=key, power=value))
            found = True
            break
    if not found:
        print(random.choice(responses_not_found))
    i+=1