#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pandas as pd
from fonctions.construire_resultats import construire_resultats

dataframe = pd.read_csv(
    os.sep.join(["static", "fr-esr-parcoursup.csv"]),
    sep=";", encoding='cp1252', low_memory=False
)

def test_construire_resultats():
    resultat = construire_resultats(
        lieu="Ile-de-France",
        choix_ville="Clichy",
        choix_etablissement="Lycée Newton-Enrea",
        dataframe=dataframe
    )

    assert isinstance(resultat, dict), "Le résultat doit être un dictionnaire"
    assert "probas" in resultat, "La clé 'probas' est manquante"
    assert "mentions" in resultat, "La clé 'mentions' est manquante"
    assert "listes" in resultat, "La clé 'listes' est manquante"
    assert resultat["mentions"]["none"] == 10, "Le calcul des mentions dans construire_resultats a un problème"
    assert len(resultat["listes"]["region"]) > 0, "La liste des régions ne doit pas être vide"
