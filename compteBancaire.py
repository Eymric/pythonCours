class CompteBancaire:
    def __init__(self, name='Dupont', solde=500):
        self.solde = solde
        self.nom = name
        self.affiche()

    def depot(self, somme):
        print('Depot de',somme, 'euros')
        self.solde = self.solde + somme
        return print('Nouveau solde après dépot:', self.solde)

    def retrait(self, somme):
        print('Retrait de',somme,'euros')
        self.solde = self.solde - somme
        return print('Nouveau solde après retrait:', self.solde)

    def affiche(self):
        return print('Le solde du compte bancaire de', self.nom, 'est de', self.solde, 'euros')

cb = CompteBancaire('Gerard', 800)
cb.retrait(100)
cb.depot(50)
cb.affiche()