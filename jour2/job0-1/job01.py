from job0 import Personne

class Auteur(Personne): 

    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.oeuvre = []

    # et générer une instance de la classe livre avec ce titre.
    def ecrireUnLivre(self,titre):
        self.oeuvre.append(titre)
        titre = Livre(titre, Auteur)

    # Une méthode “listerOeuvre” affichant dans le terminal la liste des livres écrits par l’auteur
    # Ajouter ce nouveau livre à l’oeuvre de l’auteur
    def listerOeuvre(self):
        print(self.oeuvre)

class Livre():

    def __init__(self, titre, Auteur):
        self.auteur = Auteur
        self.titre = titre
    
    def print(self):
        print(self.titre)
    # Ajouter une méthode “print” permettant d’afficher dans le terminal le titre du livre

#Résultat
a1 = Auteur('Jean','Lasalle')
a1.ecrireUnLivre('La bergerie')
a1.ecrireUnLivre('La bergerie 2')
a1.ecrireUnLivre('La bergerie 3')

livre = Livre('test' , a1)
print(a1.oeuvre)