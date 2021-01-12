

class Perso:
    """Classe qui représente un personnage"""

    def __init__(self, nom, power):
        self.nom = nom
        self.pouvoir = power
        self.hp = 100

    def afficher(self):
        print(f"Je suis {self.nom} et mon pouvoir est {self.pouvoir} !")

    def change_nom(self, nex_name):
        self.nom = nex_name

    def frappe(self, degats):
        if degats <= self.hp:
            self.hp -= degats
        else:
            self.hp = 0

    def soigne(self, soin):
        if soin <= 100 - self.hp:
            self.hp += soin
        else:
            self.hp = 100

    def en_vie(self):


thor = Perso("Thor", "foudre")
hulk = Perso("Hulk", "Force")

thor.change_nom("Olivier")

thor.afficher()



