class Personne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, prenom):
        self._prenom = prenom


    def sePresenter(self):
        print(self.nom + ' ' + self.prenom)

# p1 = Personne('Toréa','Patissier')
# p1.sePresenter()

# p2 = Personne('Abdul','Kamara')
# p2.sePresenter()