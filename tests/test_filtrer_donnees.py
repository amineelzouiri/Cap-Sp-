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
#teste BTS
    resultat_filtre = selection_infos(
        choix_dep=None,                           
        choix_etablissement="Lycée Newton-Enrea", 
        choix_fil="BTS",                          
        choix_postbac=None,                       
        choix_ville="Clichy",                     
        df_filtered=dataframe,                    
        lieu="Ile-de-France"                      
    )


    assert not resultat_filtre.empty, "Le filtre n'a trouvé aucune donnée. Vérifiez la correspondance des colonnes."

    
    assert (resultat_filtre["Région de l’établissement"] == "Ile-de-France").all()
    assert (resultat_filtre["Commune de l’établissement"] == "Clichy").all()
    assert (resultat_filtre["Département de l’établissement"] == "Hauts-de-Seine").all()

    
    assert (resultat_filtre["Établissement"] == "Lycée Newton-Enrea").all()
  
    assert (resultat_filtre_4["Filière de formation"] == "BTS").all()
   
    resultat_vide = selection_infos(lieu="Lune", df_filtered=dataframe)
    assert resultat_vide.empty, "Le filtre devrait être vide pour une région inexistante"

#test None
    resultat_aucun_filtre = selection_infos(
        choix_dep=None,
        choix_etablissement=None,
        choix_fil=None,
        choix_postbac=None,
        choix_ville=None,
        df_filtered=dataframe,
        lieu=None
    )

    assert not resultat_aucun_filtre.empty, "Sans filtre, le dataframe ne doit pas être vide"
    assert len(resultat_aucun_filtre) == len(dataframe), "Sans filtre, nous devons avoir la meme longueur car la data n'a pas été filtrée"

    resultat_region = selection_infos(lieu="Ile-de-France", df_filtered=dataframe)
    assert not resultat_region.empty, "Le filtre par région ne doit pas être vide"
    assert (resultat_region["Région de l'établissement"] == "Ile-de-France").all(), "Toutes les lignes doivent être en Ile-de-France"



# test License
    resultat_filtre_2 = selection_infos(
        choix_dep=None,
        choix_etablissement="Université Clermont Auvergne",
        choix_fil="Licence",
        choix_postbac=None,
        choix_ville="Clermont-Ferrand",
        df_filtered=dataframe,
        lieu="Auvergne-Rhône-Alpes"
    )

    assert not resultat_filtre_2.empty, "Le filtre n'a trouvé aucune donnée."
    assert (resultat_filtre_2["Région de l'établissement"] == "Auvergne-Rhône-Alpes").all()
    assert (resultat_filtre_2["Commune de l'établissement"] == "Clermont-Ferrand").all()
    assert (resultat_filtre_2["Établissement"] == "Université Clermont Auvergne").all()
    assert (resultat_filtre_4["Filière de formation"] == "Licence").all()

# test CPGE
    resultat_filtre_3 = selection_infos(
        choix_dep=None,
        choix_etablissement="Lycée Louis Barthou",
        choix_fil="CPGE",
        choix_postbac=None,
        choix_ville="Pau",
        df_filtered=dataframe,
        lieu="Nouvelle-Aquitaine"
    )   

    assert not resultat_filtre_3.empty, "Le filtre n'a trouvé aucune donnée."
    assert (resultat_filtre_3["Région de l'établissement"] == "Nouvelle-Aquitaine").all()
    assert (resultat_filtre_3["Commune de l'établissement"] == "Pau").all()
    assert (resultat_filtre_3["Établissement"] == "Lycée Louis Barthou").all()
    assert (resultat_filtre_4["Filière de formation"] == "CPGE").all()


#test ecole d'ingenieur
    resultat_filtre_4 = selection_infos(
        choix_dep=None,
        choix_etablissement="ISEN Brest",
        choix_fil="Formation d'ingénieur Bac + 5 - Bacs généraux - 2 Sciences",
        choix_postbac=None,
        choix_ville="Brest",
        df_filtered=dataframe,
        lieu="Bretagne"
    )

    assert not resultat_filtre_4.empty, "Le filtre n'a trouvé aucune donnée."
    assert (resultat_filtre_4["Région de l'établissement"] == "Bretagne").all()
    assert (resultat_filtre_4["Commune de l'établissement"] == "Brest").all()
    assert (resultat_filtre_4["Établissement"] == "ISEN Brest").all()
    assert (resultat_filtre_4["Filière de formation"] == "Formation d'ingénieur Bac + 5 - Bacs généraux - 2 Sciences").all()
