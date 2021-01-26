from configuration import CARRE

def move(structure, position, direction):
    x = position[0]
    y = position[1]
    colonne = x // CARRE
    ligne = y // CARRE
    if direction == "droite":
        if structure[ligne][colonne + 1] == "m":
            print("Bim le mur")
            return position
        elif structure[ligne][colonne + 1] == "#":
            print("Attention, caisse !")
            if structure[ligne][colonne + 2] == "_":
                print(structure[ligne])
                structure[ligne] = structure[ligne][:colonne + 2] + "#" + structure[ligne][colonne + 3:]
                structure[ligne] = structure[ligne][:colonne + 1] + "_" + structure[ligne][colonne + 2:]
                print(structure[ligne])
                position[0] += CARRE
        else:
            position[0] += CARRE
            #position = position.move(32, 0)
    if direction == "gauche":
        if structure[ligne][colonne - 1] == "m":
            print("Bim le mur")
            return position
        elif structure[ligne][colonne - 1] == "#":
            print("Attention, caisse !")
            if structure[ligne][colonne - 2] == "_":
                print(structure[ligne])
                structure[ligne] = structure[ligne][:colonne - 2] + "#" + structure[ligne][colonne - 1:]
                structure[ligne] = structure[ligne][:colonne - 1] + "_" + structure[ligne][colonne:]
                print(structure[ligne])
                position[0] -= CARRE
        else:
            position[0] -= CARRE
            #position = position.move(32, 0)
    if direction == "bas":
        if structure[ligne + 1][colonne] == "m":
            print("Bim le mur")
            return position

        elif structure[ligne + 1][colonne] == "#":
            print("Attention, caisse !")
            if structure[ligne + 2][colonne] == "_":
                print(structure[ligne])
                structure[ligne + 1] = structure[ligne + 1][:colonne] + "_" + structure[ligne + 1][colonne + 1:]
                structure[ligne + 2] = structure[ligne + 2][:colonne] + "#" + structure[ligne + 2][colonne + 1:]
                position[1] += CARRE
        else:
            position[1] += CARRE

    if direction == "haut":
        if structure[ligne - 1][colonne] == "m":
            print("Bim le mur")
            return position

        elif structure[ligne - 1][colonne] == "#":
            print("Attention, caisse !")
            if structure[ligne - 2][colonne] == "_":
                print(structure[ligne])
                structure[ligne - 1] = structure[ligne - 1][:colonne] + "_" + structure[ligne - 1][colonne + 1:]
                structure[ligne - 2] = structure[ligne - 2][:colonne] + "#" + structure[ligne - 2][colonne + 1:]
                position[1] -= CARRE

        else:
            position[1] -= CARRE
            #position = position.move(32, 0)
    print(f"Le personne se trouve actuellement en colonne {colonne} et ligne {ligne}")
    return position
