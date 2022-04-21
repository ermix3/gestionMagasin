from gestionMagasin.Magasin import Magasin
from gestionMagasin.Produit import Produit
from gestionMagasin.Livre import Livre
from gestionMagasin.CD import CD
from gestionMagasin.ProduitInexistantException import ProduitInexistantException

while True:
    print("""
    1. Ajouter un magasin
    2. Quitter
    """)
    choix = input("Votre choix: ")
    if choix == "1":
        nom = input("Nom du magasin: ")
        adresse = input("Adresse du magasin: ")
        magasin = Magasin(nom, adresse)
        while True:
            print("""
            1. Ajouter un produit
            2. Chercher un produit
            3. Supprimer un produit
            4. Afficher la liste des produits
            5. Afficher la liste des livres
            6. Afficher la liste des CDs
            7. Enregistrer les donnees
            8. Retour
            """)
            choix2 = input("Votre choix : ")
            if choix2 == "1":
                while True:
                    print("""
                    1. Ajouter un livre
                    2. Ajouter un CD
                    3. Retour""")
                    choix3 = input("Votre choix : ")
                    if choix3 == "1":
                        while True:
                            try:
                                code = int(input("code du livre : "))
                                nom = input("Titre du livre : ")
                                prix_achat = float(
                                    input("Prix d'achat du livre : "))
                                prix_vente = float(
                                    input("Prix de vente du livre : "))
                                auteur = input("Auteur du livre : ")
                                editeur = input("Editeur du livre : ")
                                nb_pages = int(
                                    input("Nombre des pages du livre : "))
                                magasin.ajouter_produit(
                                    Livre(code, nom, prix_achat, prix_vente, auteur, editeur, nb_pages))
                                break
                            except ValueError as e:
                                print("Essayer d'enter un nombre")
                    elif choix3 == "2":
                        while True:
                            try:
                                code = int(input("code du CD : "))
                                nom = input("Titre du CD : ")
                                prix_achat = float(
                                    input("Prix d'achat du CD : "))
                                prix_vente = float(
                                    input("Prix de vente du CD : "))
                                auteur = input("Auteur du CD : ")
                                interprete = input("Interprete du CD : ")
                                magasin.ajouter_produit(
                                    CD(code, nom, prix_achat, prix_vente, auteur, interprete))
                                break
                            except ValueError as e:
                                print("Essayer d'enter un nombre")
                    elif choix3 == "3":
                        break
                    else:
                        print("Choix incorrect")
            elif choix2 == "2":
                while True:
                    try:
                        num = int(
                            input("Rechercher un produit par son code: "))
                        print(magasin.chercher_produit(num))
                    except ProduitInexistantException as e:
                        print(e)
            elif choix2 == "3":
                while True:
                    try:
                        num = int(input("Supprimer un produit par son code: "))
                        magasin.supprimer_produit(num)
                        break
                    except ProduitInexistantException as e:
                        print(e)
                    except ValueError:
                        print(f"Entrer un valide code")
            elif choix2 == "4":
                if magasin.liste_produits:
                    for p in magasin.liste_produits:
                        print(magasin.liste_produits.index(p), '->', p)
                else:
                    print('accun produit a afficher. ')
            elif choix2 == "5":
                if len(magasin.liste_livres()) > 0:
                    print(magasin.liste_livres())
                else:
                    print("Aucun livre")
            elif choix2 == "6":
                if len(magasin.liste_cds()) > 0:
                    print(magasin.liste_cds())
                else:
                    print("Aucun CD")
            elif choix2 == "7":
                magasin.enregistrer_donnees()
            elif choix2 == "8":
                break
            else:
                print("Choix incorrect")
    elif choix == "2":
        break
    else:
        print("Choix incorrect")
