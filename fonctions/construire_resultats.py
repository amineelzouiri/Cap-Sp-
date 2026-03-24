#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

from fonctions.calculer_probabilites_admission import calculer_probabilites_admission
from fonctions.calculer_repartition_mentions import calculer_repartition_mentions
from fonctions.definir_listes import definir_listes
from fonctions.filtrer_donnees import filtrer_donnees


def construire_resultats(parametres: dict):
    
    df_filtered = filtrer_donnees(parametres)
    liste_filiere_agregee, liste_region, liste_etablissement, liste_de_filiere, liste_filiere_postbac = \
        definir_listes(parametres['dataframe'])

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
