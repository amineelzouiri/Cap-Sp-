#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

from fonctions.filtrer_donnees import filtrer_donnees

def mettre_a_jour_listes(param: dict):

    df_temp_filtered = filtrer_donnees(param)

    villes = sorted(df_temp_filtered["Commune de l’établissement"].dropna().unique())
    filieres = sorted(df_temp_filtered["Filière de formation"].dropna().unique())
    postbacs = sorted(df_temp_filtered["Filière de formation détaillée"].dropna().unique())

    return {"villes": villes, "filieres": filieres, "postbacs": postbacs}
