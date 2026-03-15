#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

def filtrer_donnees(choix_dep=None, choix_etablissement=None, choix_fil=None, choix_postbac=None,
                    choix_ville=None, lieu=None, df_filtered=None):
    """
    Applique successivement les filtres sélectionnés par l'utilisateur sur le DataFrame Parcoursup.

    Paramètres :
        choix_dep (str)           : filière agrégée (ex: "BTS", "Licence")
        choix_etablissement (str) : nom de l'établissement
        choix_fil (str)           : filière de formation
        choix_postbac (str)       : filière détaillée post-bac
        choix_ville (str)         : commune ou agglomération
        lieu (str)                : région
        df_filtered (DataFrame)   : DataFrame Parcoursup complet

    Retourne :
        DataFrame : sous-ensemble filtré selon les critères fournis
    """
    if lieu:
        df_filtered = df_filtered[df_filtered["Région de l'établissement"] == lieu]
    if choix_dep:
        df_filtered = df_filtered[df_filtered["Filière de formation très agrégée"] == choix_dep]
    if choix_ville:
        df_filtered = df_filtered[
            (df_filtered["Commune de l'établissement"] == choix_ville) | (df_filtered["Agglomération"] == choix_ville)]
    if choix_fil:
        df_filtered = df_filtered[df_filtered["Filière de formation"] == choix_fil]
    if choix_postbac:
        df_filtered = df_filtered[df_filtered["Filière de formation détaillée"] == choix_postbac]
    if choix_etablissement:
        df_filtered = df_filtered[df_filtered["Établissement"] == choix_etablissement]
    return df_filtered
