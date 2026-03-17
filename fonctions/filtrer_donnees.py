#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

def filtrer_donnees(param):
    """
    Applique successivement les filtres sélectionnés par l'utilisateur sur le DataFrame Parcoursup.

    Paramètres :
        choix_dep (str)           : filière agrégée (ex: "BTS", "Licence")
        choix_etablissement (str) : nom de l'établissement
        choix_fil (str)           : filière de formation
        choix_postbac (str)       : filière détaillée post-bac
        choix_ville (str)         : commune ou agglomération
        lieu (str)                : région
        dataframe (DataFrame)   : DataFrame Parcoursup complet

    Retourne :
        DataFrame : sous-ensemble filtré selon les critères fournis
    """
    dataframe = param['dataframe']
    if param['lieu']:
        dataframe = dataframe[dataframe["Région de l’établissement"] == param['lieu']]
    if param['choix_dep']:
        dataframe = dataframe[dataframe["Filière de formation très agrégée"] == param['choix_dep']]
    if param['choix_ville']:
        dataframe = dataframe[
            (dataframe["Commune de l’établissement"] == param['choix_ville']) | (dataframe["Agglomération"] == param['choix_ville'])]
    if param['choix_fil']:
        dataframe = dataframe[dataframe["Filière de formation"] == param['choix_fil']]
    if param['choix_postbac']:
        dataframe = dataframe[dataframe["Filière de formation détaillée"] == param['choix_postbac']]
    if param['choix_etablissement']:
        dataframe = dataframe[dataframe["Établissement"] == param['choix_etablissement']]
    return dataframe
