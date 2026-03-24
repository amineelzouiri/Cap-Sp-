#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

def definir_listes(dataframe):
    listes = []
    for entete in ["Filière de formation très agrégée", "Région de l’établissement", "Commune de l’établissement",
                   "Filière de formation", "Filière de formation détaillée"]:
        listes.append(sorted(dataframe[entete].dropna().unique()))
    return tuple(listes)
