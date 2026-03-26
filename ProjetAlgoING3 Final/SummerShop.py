# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 22:16:05 2023

@author: TCHAWA
"""

import Fonctions as pa
import pandas as pds # Utilisé pour la manipulation des données de la liste d'articles
from datetime import datetime # Utilisé pour afficher la date et l'heure d'achat d'un client

# Chargement de la liste des articles d'un fichier Excel d'extension CSV à un dataframe(Confère cours python pandas)

df = pds.read_csv("Stock.csv", sep=";")

print("*** Bienvenue à SUMMER SHOP ***")

# Vérifier si le client veut acheter des articles ou non
again = int(input("\nVoulez vous acheter un article ? (OUI = 0 ou NON = 1) : "))
if(again==0):
    # Facture généré avec la date du jour de l'achat
    datactuel = "facture du {} à {}.txt".format(datetime.now().strftime('%Y-%m-%d'),datetime.now().strftime('%H°%M°%S'))

    # Ouverture de la facture générée
    f = open(datactuel,"w")

    while(again == 0):
            line = "id\tLibellé\tQuantité\tPU\tPrixTotal"
            f.writelines(str(line)+"\n")
            
            # Consultation de la liste des articles
            print(df)
            
            # Choix de l'article
            i = int(input("\nQue voulez-vous acheter ? : "))
            i = i-1
            
            # Initialisation du montant total de la facture
            total=0
            
            while(i<10 and i>=0):
    
                # Sélection de la quantité à acheter
                qte = int(input("\nQuantité : "))
    
                # Calcul de la Quantité restante
                sell = pa.reste(df.iloc[i,3],qte)
                
                # Mise à jour du stock après calcul de la quantité restante
                df.iloc[i,3]=sell
                
                print("\nQuantité restante : "+str(sell))
                print("Le prix unitaire de cet article est de "+str(df.iloc[i,2]))
                
                # Calcul du prix total d'achat de l'article
                ptotal = pa.vente(df.iloc[i,2],qte)
                print("\nPrix Total : "+str(ptotal))
                
                # Incrémentation du total des achats par le prix total de l'article choisi
                total=total+ptotal
                print("\nTotal : "+str(total))
                
                
                # ligne contenant Id Libellé Quantité PrixUnitaire PrixTotal de l'article acheté
                achat = str(i)+"\t"+str(df.iloc[i,1])+"\t"+str(qte)+"\t\t"+str(df.iloc[i,2])+"\t"+str(ptotal)+"\t"
                
                # ligne de l'article choisi ajouté dans la facture
                f.writelines(str(achat)+ "\n")
                
                # Cas de Réapprovisionnement de l'article lorsque le seuil est atteint ou dépassé
                if(sell <= df.iloc[i,4]):
                    print("\nSeuil atteint ou dépassé !")
                    print("Mode Gestionnaire en cours de chargement...")
                    
                    app=int(input("\nCombien voulez vous approvisionner ? : "))
                    sell = sell + app # Qté approvisionnée ajouté à la Qté restante
                    print("\nRéapprovisionnement en cours...")
                    
                    # sell = pa.approvisionner(sell,df.iloc[i,4])
                    
                    df.iloc[i,3]=sell
                    print("Nouvelle Quantité : "+str(sell))
                
                # En cas d'achat d'un autre article ou de fin de session d'achat
                again = int(input("\nVoulez vous acheter un autre article ? ( OUI = 0 ou NON = 1) : "))
                if(again > 0):
                    i=10
                elif(again==0):
                    print(df)
                    i = int(input("Que voulez-vous acheter ? : "))
                    i = i-1
                else:
                    i=10
                    
    line1 = "\nTOTAL : \t\t\t\t"+str(total)
    f.write(str(line1))
else:
    i=10

# Mise à jour du stock des articles après une session d'achat dans un nouveau fichier CSV
df.to_csv('NewStock.csv', sep=';')

print("\nSession d'achat Terminé !")
print("\nVotre Facture vient d'etre imprimé")
print("\nMerci d'avoir choisi Summer Shop pour vos courses. A très bientôt !")

f.close()
