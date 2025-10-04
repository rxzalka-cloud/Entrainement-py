for Num in range(1, 11):             # pour chaque table (de 1 à 10)
    print("Table de", Num)           # affiche le titre de la table
    for multiple in range(1, 11):    # pour chaque multiple (de 1 à 10)
        print(Num, "x", multiple, "=", Num * multiple)
    print("----")                    # sépare les tables
