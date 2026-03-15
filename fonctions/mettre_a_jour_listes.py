#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

from fonctions.filtrer_donnees import filtrer_donnees

def mettre_a_jour_listes(lieu=None, choix_dep=None, choix_ville=None, choix_fil=None, dataframe=None):
    """
    Met à jour dynamiquement les listes déroulantes du simulateur en fonction
    des filtres déjà sélectionnés par l'utilisateur (requête AJAX).

    Paramètres :
        lieu (str)       : région sélectionnée
        choix_dep (str)  : filière agrégée sélectionnée
        choix_ville (str): commune sélectionnée
        choix_fil (str)  : filière sélectionnée
        dataframe (DataFrame) : DataFrame Parcoursup complet

    Retourne :
        dict : {'villes': list, 'filieres': list, 'postbacs': list}
    """
    df = dataframe.copy()
    df_temp_filtered = filtrer_donnees(
        lieu=lieu, choix_dep=choix_dep, choix_ville=choix_ville, choix_fil=choix_fil, df_filtered=df)

    villes = sorted(df_temp_filtered["Commune de l'établissement"].dropna().unique())
    filieres = sorted(df_temp_filtered["Filière de formation"].dropna().unique())
    postbacs = sorted(df_temp_filtered["Filière de formation détaillée"].dropna().unique())

    return {"villes": villes, "filieres": filieres, "postbacs": postbacs}
