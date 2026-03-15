#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pandas as pd
from fonctions.calculer_probabilites_admission import calculer_probabilites_admission

dataframe = pd.read_csv(
    os.sep.join(["static", "fr-esr-parcoursup.csv"]),
    sep=";", encoding='cp1252', low_memory=False
)

def test_calculer_probabilites_admission():
    tableau_vide = dataframe[dataframe["Établissement"] == "Etablissement Inexistant"]
    resultat_vide = calculer_probabilites_admission(tableau_vide)
    assert resultat_vide == {"general": 0, "pro": 0, "tech": 0}, \
        "Un DataFrame vide doit retourner des zéros et non une erreur"

    proba_globales = calculer_probabilites_admission(dataframe)

    assert "general" in proba_globales, "La clé 'general' est absente du dictionnaire"
    assert isinstance(proba_globales["general"], float), "Le résultat doit être un nombre décimal"

    pourcentage_general = proba_globales["general"]
    assert 0 <= pourcentage_general <= 100, \
        f"Le pourcentage ({pourcentage_general}) doit être compris entre 0 et 100"
