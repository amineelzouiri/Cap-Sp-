#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pandas as pd
from fonctions.filtrer_donnees import filtrer_donnees

dataframe = pd.read_csv(
    os.sep.join(["static", "fr-esr-parcoursup.csv"]),
    sep=";", encoding='cp1252', low_memory=False
)

def test_filtrer_donnees():
    resultat_filtre = filtrer_donnees(
        choix_dep="BTS",
        choix_etablissement="Lycée Newton-Enrea",
        choix_fil=None,
        choix_postbac=None,
        choix_ville="Clichy",
        dataframe=dataframe,
        lieu="Ile-de-France"
    )

    assert not resultat_filtre.empty, "Le filtre n'a trouvé aucune donnée, vérifiez les paramètres"
    assert (resultat_filtre["Région de l'établissement"] == "Ile-de-France").all(), \
        "Certaines lignes ne correspondent pas à la région Ile-de-France"
    assert (resultat_filtre["Commune de l'établissement"] == "Clichy").all(), \
        "Certaines lignes ne correspondent pas à la ville de Clichy"
    assert (resultat_filtre["Filière de formation très agrégée"] == "BTS").all(), \
        "Certaines lignes ne correspondent pas à la filière BTS"

    resultat_vide = filtrer_donnees(lieu="Mars", dataframe=dataframe)
    assert resultat_vide.empty, "Le filtre devrait être vide pour une région inexistante"
