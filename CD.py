from gestionMagasin.Produit import Produit


class CD(Produit):
    nb_CD = 0
    def __init__(self,code:int, nom:str, prix_achat:float, prix_vente:float,auteur:str, interprete:str):
        super().__init__(code, nom, prix_achat, prix_vente)
        self.__auteur = auteur
        self.__interprete = interprete
        CD.nb_CD += 1

    def __del__(self):
        CD.nb_CD -= 1

    @property
    def auteur(self)->str:
        return self.__auteur

    @property
    def interprete(self)->str:
        return self.__interprete

    @interprete.setter
    def interprete(self, interprete)->None:
        self.__interprete = interprete

    @auteur.setter
    def auteur(self, auteur)->None:
        self.__auteur = auteur

    def __str__(self)->str:
        return f'{super().__str__()}, Auteur: {self.__auteur}, Interprete: {self.__interprete}.'
