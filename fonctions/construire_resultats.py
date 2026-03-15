#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

from fonctions.calculer_probabilites_admission import calculer_probabilites_admission
from fonctions.calculer_repartition_mentions import calculer_repartition_mentions
from fonctions.definir_listes import definir_listes
from fonctions.filtrer_donnees import filtrer_donnees

def construire_resultats(lieu=None, choix_dep=None, choix_ville=None, choix_fil=None, choix_postbac=None,
                         choix_etablissement=None, dataframe=None):
    """
    Agrège toutes les données nécessaires à l'affichage du simulateur Parcoursup :
    probabilités d'admission, répartition des mentions et listes des filtres disponibles.

    Paramètres :
        lieu, choix_dep, choix_ville, choix_fil, choix_postbac, choix_etablissement (str) : filtres
        dataframe (DataFrame) : DataFrame Parcoursup complet

    Retourne :
        dict : résultats complets pour affichage dans le template index.html
    """
    df = dataframe.copy()
    df_filtered = filtrer_donnees(choix_dep, choix_etablissement, choix_fil, choix_postbac, choix_ville, lieu, df)
    liste_filiere_agregee, liste_region, liste_etablissement, liste_de_filiere, liste_filiere_postbac = definir_listes(dataframe)

    return {
        "probas": calculer_probabilites_admission(df_filtered),
        "mentions": calculer_repartition_mentions(df_filtered),
        "listes": {
            "filiere_agregee": liste_filiere_agregee,
            "region": liste_region,
            "etablissement": liste_etablissement,
            "filiere_detaillee": liste_de_filiere,
            "filiere_postbac": liste_filiere_postbac
        },
        "result_count": len(df_filtered)
    }
