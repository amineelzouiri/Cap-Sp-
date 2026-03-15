#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pandas as pd
from fonctions.calculer_repartition_mentions import calculer_repartition_mentions

dataframe = pd.read_csv(
    os.sep.join(["static", "fr-esr-parcoursup.csv"]),
    sep=";", encoding='cp1252', low_memory=False
)

def test_calculer_repartition_mentions():
    df_newton = dataframe[dataframe["Établissement"] == "Lycée Newton-Enrea"]

    resultat = calculer_repartition_mentions(df_newton)

    assert resultat["tb"] == 19.0, f"Attendu 19.0, reçu {resultat['tb']}"
    assert resultat["b"] == 25.0, "Erreur sur la mention Bien"
    assert resultat["none"] == 54.0, "Erreur sur la catégorie Sans Mention"
    assert len(resultat) == 4, "Le dictionnaire doit contenir 4 types de mentions"
