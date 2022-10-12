#!/usr/bin/python3
# -*- coding: utf-8 -*-

# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-12 09:48:02
#  * @modify date 2022-10-12 09:48:02
#  * @desc [TP1_Exo3]
#  */

# ==================================================
# ==================== Consigne ====================
# ==================================================

# Equation du second degré
# from math import sqrt Ensuite:
# Calcul des racines réelles du trinôme: ax2 + bx + c = 0 
# Juste après l’en-tête du fichier, insérez l’instruction:
#   • Saisir trois nombres flottants correspondants aux coefficients et les stocker dans des variables a, b et c.
#   • Calculer la valeur du discriminant, delta.

#   • En testant la valeur de delta(négatif, nul ou positif), afficher qu’il n’existe pas de racine réelle, ou la valeur de la racine réelle double, ou enfin les valeurs des deux racines réelles. N’oubliez pas de formater proprement vos affichages.

# ==================================================
# ==================== Solution ====================
# ==================================================

from math import sqrt

def discriminant(a, b, c):
    return b**2 - 4 * a * c


def racineReelleDouble(a, b):
    return -b / (2 * a)


def racineReelle(a, b, c):
    delta = discriminant(a, b, c)
    return (-b - sqrt(delta)) / (2 * a), (-b + sqrt(delta)) / (2 * a)


def main():
    a = float(input("a : "))
    b = float(input("b : "))
    c = float(input("c : "))

    delta = discriminant(a, b, c)

    if delta < 0:
        print("Il n'existe pas de racine réelle")
    elif delta == 0:
        print("Il existe une racine réelle double : " + str(racineReelleDouble(a, b)))
    else:
        print("Il existe deux racines réelles : " + str(racineReelle(a, b, c)))


if __name__ == "__main__":
    main()