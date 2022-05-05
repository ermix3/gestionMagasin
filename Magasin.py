from gestionMagasin.ProduitInexistantException import ProduitInexistantException
from gestionMagasin.Produit import Produit
from gestionMagasin.Livre import Livre
from gestionMagasin.CD import CD


class Magasin:
    liste_produits = []

    def __init__(self, nom: str = None, adresse: str = None) -> None:
        self.__nom = nom
        self.__adresse = adresse

    def __str__(self) -> str:
        return f'Magasin : {self.nom} ; adresse: {self.adresse}; list des produits: {[p.__str__() for p in self.liste_produits]}'

    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def adresse(self) -> str:
        return self.__adresse

    @nom.setter
    def nom(self, nom) -> None:
        self.__nom = nom

    @adresse.setter
    def adresse(self, adresse) -> None:
        self.__adresse = adresse

    def ajouter_produit(self, produit) -> None:
        try:
            if type(self.chercher_produit(produit.code)) in (Livre, CD):
                print(f"Le produit {produit.code} existe déjà")
        except ProduitInexistantException:
            self.liste_produits.append(produit)
            print(f"Le produit de code '{produit.code}' a été ajouté")

    def supprimer_produit(self, code) -> None:
        try:
            if type(self.chercher_produit(code)) in (Livre, CD):
                self.liste_produits.remove(self.chercher_produit(code))
                print(f"Le produit de code '{code}' a été supprimé")
        except ProduitInexistantException:
            print(f"Le produit de code '{code}' n'existe pas")

    def chercher_produit(self, code) -> Produit:
        for p in self.liste_produits:
            if p.code == code:
                return p
            
        raise ProduitInexistantException(
            f"Le produit de code '{code}' n'existe pas")

    def liste_livres(self) -> list:
        return [produit.__str__() for produit in self.liste_produits if type(produit) == Livre]

    def liste_cds(self) -> list:
        return [produit.__str__() for produit in self.liste_produits if type(produit) == CD]

    def enregistrer_donnees(self) -> None:
        with open(f"{self.nom}.txt", "w") as fichier:
            fichier.write(
                f"Magasin: {self.nom}\nAdresse: {self.adresse}\nproduit:\n{[produit.__str__() for produit in self.liste_produits]}")
        print('les donnes a ete enregistrer')
