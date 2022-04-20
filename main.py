from gestionMagasin.Magasin import Magasin
from gestionMagasin.Produit import Produit
from gestionMagasin.Livre import Livre
from gestionMagasin.CD import CD



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
            7. Sauvegarder les donnees
            8. Quitter
            """)
            choix2 = input("Votre choix : ")
            if choix2 == "1":
                print("1. Ajouter un livre")
                print("2. Ajouter un CD")
                choix3 = input("Votre choix : ")
                if choix3 == "1":
                    code = int(input("code du livre : "))
                    nom = input("Titre du livre : ")
                    prix_achat = float(input("Prix d'achat du livre : "))
                    prix_vente = float(input("Prix de vente du livre : "))
                    auteur = input("Auteur du livre : ")
                    editeur = input("Editeur du livre : ")
                    nb_pages = int(input("Nombre des pages du livre : "))
                    magasin.ajouter_produit(Livre(code, nom, prix_achat, prix_vente, auteur,editeur,nb_pages ))
                elif choix3 == "2":
                    code = int(input("code du CD : "))
                    nom = input("Titre du CD : ")
                    prix_achat = float(input("Prix d'achat du CD : "))
                    prix_vente = float(input("Prix de vente du CD : "))
                    auteur = input("Auteur du CD : ")
                    interprete = input("Interprete du CD : ")
                    magasin.ajouter_produit(CD(code, nom,prix_achat, prix_vente, auteur, interprete))
                else:
                    print("Choix incorrect")
            elif choix2 == "2":
                print("1. Chercher un livre")
                print("2. Chercher un CD")
                choix3 = input("Votre choix : ")
                if choix3 == "1":
                    num = input("Numéro du livre : ")
                    magasin.chercher_produit(num)
            elif choix2 == "3":
                magasin.supprimer_produit(1)
            elif choix2 == "4":
                for p in magasin.liste_produits:
                    print(magasin.liste_produits.index(p),p)
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

