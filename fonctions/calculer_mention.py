#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

def calculer_mention(colonne_mention, data):
    capacite = data["Capacité de l’établissement par formation"]
    return round(sum(capacite * data[colonne_mention] / 100) / sum(capacite) * 100, 2)
