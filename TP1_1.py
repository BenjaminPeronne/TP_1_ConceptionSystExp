#!/usr/bin/python3
# -*- coding: utf-8 -*-

# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-12 09:48:02
#  * @modify date 2022-10-12 09:48:02
#  * @desc [TP1_Exo1]
#  */

# ==================================================
# ==================== Consigne ====================
# ==================================================

# Calculs de l'aire d'un rectangle
#   • Saisir deux valeurs flottantes dans deux variables largeur et longueur.
#   • Calculer l’aire de la surface correspondante et stockez là dans une variable aire.
# •  Réaliser un affichage propre pour donner le résultat du calcul.


# ==================================================
# ==================== Solution ====================
# ==================================================

def aireRectangle(largeur, longueur):
    return largeur * longueur


def main():
    largeur = float(input("Largeur : "))
    longueur = float(input("Longueur : "))
    aire = aireRectangle(largeur, longueur)
    print("L'aire du rectangle est de : " + str(aire))


if __name__ == "__main__":
    main()
