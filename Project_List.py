liste = []
menu = """Choisissez parmi les options suivantes :
1: Ajouter un element a la liste
2: Supprimer un element a la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
Votre choix : """
menu_choice  = ["1","2","3","4","5"]
while True:
    user_choice = ""
    while user_choice not in menu_choice:
        user_choice = input(menu)
        if user_choice not in menu_choice:
            print("\nVeuillez choisir une option valide...\n")
    if user_choice == "1":
        item = input("\nEntrer l'element a ajouter : ")
        liste.append(item)
        print(f"\nL'element {item} a bien ete ajoute a la liste.")
    elif user_choice == "2":
        item = input("\nEntrer l'element a supprimer : ")
        if item in liste:
            liste.remove(item)
            print(f"\nL'element {item} a bien ete supprimer.")
        else:
            print(f"\nL'element {item} ne se trouve pas dans la liste.")
    elif user_choice == "3":
        if liste:
            print("\nVoici votre liste :")
            for i,item in enumerate(liste, 1):
                print(f"{i}. {item}")
        else:
            print("\nVotre liste est vide.")
    elif user_choice == "4":
        liste.clear()
        print("\nVotre liste a bien ete videe de son contenu.")
    else:
        print("\nAu revoir!")
        break
    print("--" * 50)