#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

def calculer_probabilites_admission(df_filtered):
    
    if df_filtered.empty:
        return {"general": 0, "pro": 0, "tech": 0}

    general = round(df_filtered["% d’admis néo bacheliers généraux"].mean(), 2)
    technologique = round(df_filtered["% d’admis néo bacheliers technologiques"].mean(), 2)
    professionnel = round(df_filtered["% d’admis néo bacheliers professionnels"].mean(), 2)

    return {
        "general": general,
        "tech": technologique,
        "pro": professionnel
    }
