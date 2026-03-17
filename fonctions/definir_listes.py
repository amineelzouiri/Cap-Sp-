#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

def definir_listes(dataframe):
    """
    Génère les 5 listes de valeurs uniques triées utilisées pour
    alimenter les menus déroulants du simulateur Parcoursup.

    Paramètre :
        dataframe (DataFrame) : DataFrame Parcoursup complet

    Retourne :
        tuple : (filières agrégées, régions, communes, filières, filières détaillées)
    """
    listes = []
    for entete in ["Filière de formation très agrégée", "Région de l’établissement", "Commune de l’établissement",
                   "Filière de formation", "Filière de formation détaillée"]:
        listes.append(sorted(dataframe[entete].dropna().unique()))
    return tuple(listes)
