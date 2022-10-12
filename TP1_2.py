#!/usr/bin/python3
# -*- coding: utf-8 -*-

# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-12 09:50:44
#  * @modify date 2022-10-12 09:50:44
#  * @desc [TP1_Exo2]
#  */

# ==================================================
# ==================== Consigne ====================
# ==================================================

# Somme de deux résistances
#   • Saisir deux valeurs flottantes de résistances dans des variables r1 et r2 en indiquant l’unité dans le message(on peut utiliser "\u2126" pour afficher un joli Ω)
#   • effectuer l’affichage formaté(deux chiffres significatifs) de la résistance équivalente en série et en parallèle. Ne pas oublier l’unité.


# ==================================================
# ==================== Solution ====================
# ==================================================

def resistanceSerie(r1, r2):
    return r1 + r2


def resistanceParallele(r1, r2):
    return r1 * r2 / (r1 + r2)


def main():
    r1 = float(input("R1 : "))
    r2 = float(input("R2 : "))

    print("Résistance en série : " + "{:.2f}".format(resistanceSerie(r1, r2)) + " \u2126")
    print("Résistance en parallèle : " + "{:.2f}".format(resistanceParallele(r1, r2)) + " \u2126")


if __name__ == "__main__":
    main()
