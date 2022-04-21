class Produit:
    nombre_produits = 0

    def __init__(self, code: int = None, nom: str = None, prix_achat: float = None, prix_vente: float = None) -> None:
        self.__code = code
        self.__nom = nom
        self.__prix_achat = prix_achat
        self.__prix_vente = prix_vente
        Produit.nombre_produits += 1

    def __del__(self):
        Produit.nombre_produits -= 1

    @property
    def code(self) -> int:
        return self.__code

    @code.setter
    def code(self, code: int) -> None:
        self.__code = code

    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str) -> None:
        self.__nom = nom

    @property
    def prix_achat(self) -> float:
        return self.__prix_achat

    @prix_achat.setter
    def prix_achat(self, prix_achat: float) -> None:
        self.__prix_achat = prix_achat

    @property
    def prix_vente(self) -> float:
        return self.__prix_vente

    @prix_vente.setter
    def prix_vente(self, prix_vente: float) -> None:
        self.__prix_vente = prix_vente

    def __str__(self) -> str:
        return f"Code: {self.__code}, Nom: {self.__nom}, Prix de vente: {self.__prix_vente}, Prix d'achat: {self.__prix_achat}"

    def __eq__(self, other) -> bool:
        """
        Compare les deux produits par leur nom.
        :param other: deuxieme Produit
        :return: boolean valeur de comparaison
        """
        return self.__nom == other.nom
