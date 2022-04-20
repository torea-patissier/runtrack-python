#Importer Personne
from job0 import Personne

#Créer une classe “Auteur” héritant de la classe “Personne” recevant un nom et un prénom en paramètre de construction.
class Auteur(Personne):

    #La classe Auteur devra posséder une collection de livres nommée "œuvre" en attribut ainsi
    def __init__(self, nom, prenom, oeuvre):
        Personne.__init__(self, nom, prenom)
        self.oeuvre = oeuvre
    
    @property
    def oeuvre(self):
        return self.oeuvre

    @oeuvre.setter
    def oeuvre(self, oeuvre):
        self._oeuvre = oeuvre
    
    #  qu’une méthode “listerOeuvre” affichant dans le terminal la liste des livres écrits par l’auteur.
    def listerOeuvre(self):
        print('Afficher la liste des livres écrits par l\'auteur')

    #Ajouter à la classe Auteur une méthode “ecrireUnLivre” prenant en paramètre un titre de livre à écrire
    #  et générer une instance de la classe Livre avec ce titre. Ajouter ce nouveau livre à l’oeuvre de l’auteur
    def ecrireUnLivre(self, titre):
        print(titre)

#Créer une classe “Livre” avec comme attribut un “titre” qu’elle reçoit en paramètre à la construction et une référence vers une classe “Auteur”.
class Livre(Auteur):

    def __init__(self,nom,prenom,oeuvre,titre):
        Auteur.__init__(self,nom,prenom,oeuvre)
        self.titre = titre

    @property
    def titre(self):
        return self.titre
    
    @titre.setter
    def titre(self, titre):
        self._titre = titre 

    # Ajouter une méthode “print” permettant d’afficher dans le terminal le titre du livre.
    def print(self):
        print('Titre du livre : ' + self.titre)
