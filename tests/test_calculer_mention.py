#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pandas as pd
from fonctions.calculer_mention import calculer_mention

dataframe = pd.read_csv(
    os.sep.join(["static", "fr-esr-parcoursup.csv"]),
    sep=";", encoding='cp1252', low_memory=False
)

def test_calculer_mention():
    colonne = "% d'admis néo bacheliers avec mention Bien au bac"

    resultat = calculer_mention(colonne, dataframe.head(10))

    assert 0 <= resultat <= 100, "Le résultat doit être compris entre 0 et 100"
    assert isinstance(resultat, float), "Le résultat doit être un nombre décimal"
