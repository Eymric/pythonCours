class DateNaissance:
    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def ToString(self):
        return print(self.jour,'/',self.mois,'/',self.annee)

class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def afficher(self):
        return pprint('Nom:', self.nom, \n 'Prenom:', self.prenom, \n 'Date de naissance:', DateNaissance() )

a = Personne('A', 'B')
a.afficher