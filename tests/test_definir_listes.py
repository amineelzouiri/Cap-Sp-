#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pandas as pd
from fonctions.definir_listes import definir_listes

dataframe = pd.read_csv(
    os.sep.join(["static", "fr-esr-parcoursup.csv"]),
    sep=";", encoding='cp1252', low_memory=False
)

def test_definir_listes():
    resultat_listes = definir_listes(dataframe)

    assert isinstance(resultat_listes, tuple), "Le résultat doit être un tuple"
    assert len(resultat_listes) == 5, "Il doit y avoir exactement 5 listes de filtres"

    liste_regions = resultat_listes[1]
    liste_communes = resultat_listes[2]

    assert len(liste_regions) > 0, "La liste des régions ne doit pas être vide"
    assert len(liste_communes) > 0, "La liste des communes ne doit pas être vide"
    assert liste_regions == sorted(liste_regions), "La liste des régions doit être triée alphabétiquement"
