from gestionMagasin.Produit import Produit


class Livre(Produit):
    nombre_livres= 0
    def __init__(self, code:int, nom:str, prix_achat:float, prix_vente:float, auteur:str, editeur:str, nb_pages:int):
        super().__init__(code, nom, prix_achat, prix_vente)
        self.__auteur = auteur
        self.__editeur = editeur
        self.__nb_pages = nb_pages
        Livre.nombre_livres += 1

    def __del__(self):
        Livre.nombre_livres -= 1

    def __str__(self)-> str:
        return f'{super().__str__()}, Auteur: {self.__auteur}, Editeur: {self.__editeur}, Nombre de pages:  {self.__nb_pages}.'

    @property
    def auteur(self)->str:
        return self.__auteur

    @property
    def editeur(self)->str:
        return self.__editeur

    @property
    def nb_pages(self)->int:
        return self.__nb_pages

    @auteur.setter
    def auteur(self, auteur)->None:
        self.__auteur = auteur

    @editeur.setter
    def editeur(self, editeur)->None:
        self.__editeur = editeur

    @nb_pages.setter
    def nb_pages(self, nb_pages)->None:
        self.__nb_pages = nb_pages

    def calculer_cout(self)->str:
        """
        Calculer le cout d'un livre en fonction du nombre de pages.
        :return: chaine de charactere représentant le cout du livre.
        """
        return f"{self.__nb_pages * 1.95} dhs"