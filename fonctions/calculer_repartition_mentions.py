#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

from fonctions.calculer_mention import calculer_mention

def calculer_repartition_mentions(df_filtered):
    """
    Calcule la répartition pondérée des mentions du baccalauréat
    parmi les néo-bacheliers admis dans les formations filtrées.

    Paramètre :
        dataframe (DataFrame) : DataFrame filtré selon les critères de l'utilisateur

    Retourne :
        dict : {'tb': float, 'b': float, 'ab': float, 'none': float}
               Retourne des zéros si le DataFrame est vide.
    """
    if df_filtered.empty:
        return {"tb": 0, "b": 0, "ab": 0, "none": 0}

    sans_mention = calculer_mention(
        colonne_mention="% d’admis néo bacheliers sans mention au bac", data=df_filtered)
    assez_bien = calculer_mention(
        colonne_mention="% d’admis néo bacheliers avec mention Assez Bien au bac", data=df_filtered)
    bien = calculer_mention(
        colonne_mention="% d’admis néo bacheliers avec mention Bien au bac", data=df_filtered)
    tresbien_simple = calculer_mention(
        colonne_mention="% d’admis néo bacheliers avec mention Très Bien au bac", data=df_filtered)
    tresbien_felic = calculer_mention(
        colonne_mention="% d’admis néo bacheliers avec mention Très Bien avec félicitations au bac", data=df_filtered)
    tres_bien = round(tresbien_simple + tresbien_felic, 2)

    return {"tb": tres_bien, "b": bien, "ab": assez_bien, "none": sans_mention}
