#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

def filtrer_donnees(param):
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
