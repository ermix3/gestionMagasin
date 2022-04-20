# Projet Gestion des produits d'un Magasin
## 1- Class Produit 
  > qui design les attribus et les comportements des produits dans la magasin comme
  - Code c'est le code du produit 
  - Nom c'est le nom du produit
  - Prix_Vente c'est le prix de vente du produit
  - Prix_Achat c'est le prix d'achat du produit

### 1-1. Class Livre
  > class qui herite de la class produit avec des attributs 
  - auteur du livre
  - editeur du livre
  - nb_pages c'est le nombre de la page du livre
### 1-2. Class CD
  > class qui herite de la class produit avec des attributs
  - auteur du CD
  - interprete du CD
## 2- Class Magasin
  > class contient les inforamtions sur la magasin comme attributs
  - Nom de la magasin
  - Adresse de la magasin
  - Listes des produits dans le stock
  > plus de ca on a des methods pour faire des operations sur les produits comme
  - Ajouter_produit()
  - Suprimer_produit()
  - Chercher_produit()
  - ...