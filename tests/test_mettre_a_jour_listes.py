#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pandas as pd
from fonctions.mettre_a_jour_listes import mettre_a_jour_listes

dataframe = pd.read_csv(
    os.sep.join(["static", "fr-esr-parcoursup.csv"]),
    sep=";", encoding='cp1252', low_memory=False
)

def test_mettre_a_jour_listes():
    resultat = mettre_a_jour_listes(lieu="Ile-de-France", dataframe=dataframe)

    assert "villes" in resultat, "La clé 'villes' est absente"
    assert isinstance(resultat["villes"], list), "Le résultat doit contenir des listes"
    assert "Clichy" in resultat["villes"], "Clichy devrait être dans la liste des villes d'Ile-de-France"

    villes = resultat["villes"]
    assert villes == sorted(villes), "La liste des villes n'est pas triée alphabétiquement"

    resultat_vide = mettre_a_jour_listes(lieu="REGION_INEXISTANTE", dataframe=dataframe)
    assert resultat_vide["villes"] == [], "La liste des villes devrait être vide pour une région inexistante"
