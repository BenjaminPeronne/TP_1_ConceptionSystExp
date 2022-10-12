#!/usr/bin/python3
# -*- coding: utf-8 -*-

# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-12 09:48:02
#  * @modify date 2022-10-12 09:48:02
#  * @desc [TP1_Exo4]
#  */

# ==================================================
# ==================== Consigne ====================
# ==================================================

# Calcul dela divison euclidienne

# 1. Saisir deux entiers positifs a et b ;
# 2. calculer le quotient q et le reste r ;
# 3. afficher la division euclidienne. Avec par exemple 45 et 11, on doit obtenir :
# Ce calcul nécessite l'utilisation de la racine carrée. La fonctionsqrtappartient évidemment au modulemath. Regardez sa syntaxe exacte dans la documentation (ou tapez help(sqrt) dans un interpréteur)
# Division euclidienne: 45 = 11*4 + 1

# ==================================================
# ==================== Solution ====================
# ==================================================

from math import sqrt


def divisionEuclidienne(a, b):
    q = int(a / b)
    r = a % b
    return q, r


def main():
    a = int(input("a : "))
    b = int(input("b : "))
    q, r = divisionEuclidienne(a, b)
    print("\n")
    print(" >>>> Division euclidienne: " + str(a) + " = " + str(b) + "*" + str(q) + " + " + str(r) + "\n")


if __name__ == "__main__":
    main()
