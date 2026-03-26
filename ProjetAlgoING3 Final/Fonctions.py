# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

# Calcule le prix total de la vente d'un article
def vente(pu,qte):
    v = pu*qte
    return v;     

# Calcule la quantité restante après vente d'un article
def reste(qte,a):
    s = qte - a;  #Quantité en Stock - Quantité vendu = Quantité restante
    return s

#Effectue l'approvisionnenment automatique du stock d'un article après vente(Pas utilisé)
# def approvisionner(qte,seuil):
       # while (qte <= seuil):
            # qte = qte + (2*qte); #Lorsque le seuil est atteint ou dépassé(Stock non vide)
            # if(qte == 0):
                # qte = qte + 1000; #Lorsque le stock est vide
        # return qte;


