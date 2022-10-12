#!/usr/bin/python3
# -*- coding: utf-8 -*-

# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-12 09:48:02
#  * @modify date 2022-10-12 09:48:02
#  * @desc [TP1_Exo5]
#  */

# ==================================================
# ==================== Consigne ====================
# ==================================================

# Règle logiques

# Principe
# Le contribuable peut, s'il le souhaite, opter pour le prélèvement de chacun de ses impôts, à la date limite de paiement qui figure sur l'avis d'imposition.
# Pour l'impôt sur le revenu, le contribuable paiera son impôt de 2010, sur ses revenus perçus en 2009, en 1 seule fois:
# • si le montant de son impôt de 2009, sur ses revenus perçus en 2008, était inférieur à 337 €,
# • ou s'il est imposé pour la première fois en 2010, sur ses revenus perçus en 2009,
# • ou si son impôt de 2009, sur ses revenus perçus en 2008, a été mis en recouvrement après le 15 avril 2010 (la date de mise en recouvrement doit figurer sur l'avis d'imposition),
# • ou s'il n'a pas été imposable en 2009, sur ses revenus perçus en 2008, même s'il a déjà été imposé les années précédentes.
# • À partir de ce texte, identifiez les différentes informations nécessaires pour savoir si le contribuable paiera son impôt obligatoirement en une seule fois. Associez une variable à chaque information, associée à une valeur possible.
# Écrivez-la ou les expressions logiques, utilisant les variables que vous avez définies,
# et permettant de connaître la décision sur le paiement obligatoire en une seule fois.

# ==================================================
# ==================== Solution ====================
# ==================================================

def main():
    # Déclaration des variables
    impot2009 = float(input("Impôt de 2009 : "))
    # impot2010 = float(input("Impôt de 2010 : "))
    dateMiseEnRecouvrement = input("Date de mise en recouvrement : ")
    dateLimitePaiement = input("Date limite de paiement : ")
    estImpose = input("Est imposé ? (Oui/Non) : ")
    estPremiereImpot = input("Est imposé pour la première fois ? (Oui/Non) : ")

    # Calcul de la décision
    decision = impot2009 < 337 or estPremiereImpot == "Oui" or dateMiseEnRecouvrement > dateLimitePaiement or estImpose == "Non"

    # Affichage de la décision
    print("Le contribuable paiera son impôt obligatoirement en une seule fois : " + str(decision))


if __name__ == "__main__":
    main()
