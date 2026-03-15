<div align="center">

<img src="https://cdn-icons-png.flaticon.com/512/16533/16533390.png" width="120" alt="Cap Spé Logo"/>

# 🎓 Cap Spé

### *L'orientation réinventée pour les élèves de seconde*

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Mistral AI](https://img.shields.io/badge/Mistral_AI-Agent-FF7000?style=for-the-badge&logo=mistral&logoColor=white)](https://mistral.ai)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.x-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg?style=for-the-badge)](LICENSE.txt)

<br/>

> 💡 **Cap Spé** est une application web qui aide les élèves de seconde à choisir leurs spécialités de première grâce à un chatbot IA, un simulateur Parcoursup et des ressources pédagogiques.

<br/>

---

</div>

## 📋 Table des matières

- [✨ Fonctionnalités](#-fonctionnalités)
- [🛠️ Stack technique](#️-stack-technique)
- [🚀 Installation et lancement](#-installation-et-lancement)
- [📁 Structure du projet](#-structure-du-projet)
- [🤖 Le chatbot IA](#-le-chatbot-ia)
- [📊 Le simulateur Parcoursup](#-le-simulateur-parcoursup)
- [🧪 Lancer les tests](#-lancer-les-tests)
- [👥 Équipe](#-équipe)

---

## ✨ Fonctionnalités

<div align="center">

| 🤖 Chatbot IA | 📚 Spécialités | 📊 Simulateur | 💬 Conseils |
|:---:|:---:|:---:|:---:|
| Agent Mistral spécialisé en orientation scolaire | Présentation claire de toutes les spécialités de première | Simulateur Parcoursup basé sur les données officielles | Témoignages et conseils d'élèves |
| Répond à toutes vos questions sur les parcours | Programmes, débouchés, combinaisons recommandées | Probabilités d'admission par filière, région, mention | Retours d'expérience concrets |

</div>

---

## 🛠️ Stack technique

```
Cap Spé
├── 🐍  Back-end    →  Python 3 + Flask
├── 🤖  IA          →  API Mistral AI (mistral-small-latest)
├── 📊  Données     →  Pandas + CSV Parcoursup officiel (data.gouv.fr)
├── 🎨  Front-end   →  HTML5 + Tailwind CSS + JavaScript
└── 🔐  Config      →  python-dotenv (.env)
```

---

## 🚀 Installation et lancement

> ⚠️ **Clé API non fournie** — Le chatbot nécessite une clé API Mistral pour fonctionner en local.
> Vous pouvez tester le chatbot directement en ligne sur **[capspe.fr](https://capspe.fr)** 🌐

---

<details>
<summary>🔵 &nbsp;<b>Option A — Via Git</b></summary>
<br>

**1️⃣ Cloner le dépôt**
```bash
git clone https://github.com/amineelzouiri/Cap-Sp-
cd Cap-Sp-
```

**2️⃣ Installer les dépendances**
```bash
pip install -r requirements.txt
```

**3️⃣ Configurer la clé API**

Créez un fichier `.env` à la racine du projet :
```env
API_KEY=votre_clé_api_mistral_ici
```

**4️⃣ Lancer l'application**
```bash
python app.py
```

</details>

---

<details>
<summary>🟣 &nbsp;<b>Option B — Via ZIP</b></summary>
<br>

**1️⃣ Télécharger le projet**

Sur GitHub : bouton vert **"Code"** → **"Download ZIP"** → extraire le dossier.

**2️⃣ Installer les dépendances**
```bash
pip install -r requirements.txt
```

**3️⃣ Configurer la clé API**

Créez un fichier `.env` à la racine du dossier extrait :
```env
API_KEY=votre_clé_api_mistral_ici
```

**4️⃣ Lancer l'application**
```bash
python app.py
```

</details>

---

✅ Ouvrez votre navigateur à l'adresse : **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

## 📁 Structure du projet

```
2026_[ID]_cap-spe/
│
├── 📄 app.py                               ← Point d'entrée de l'application Flask
├── 📄 requirements.txt                     ← Dépendances Python
├── 📄 licence.txt                          ← Licence GPL v3+
├── 📄 README.md                            ← Ce fichier
│
├── 📁 fonctions/                           ← Modules Python (1 fichier = 1 fonction)
│   ├── 📄 definir_listes.py               ← Génère les listes des filtres déroulants
│   ├── 📄 filtrer_donnees.py              ← Applique les filtres sur le DataFrame
│   ├── 📄 calculer_mention.py             ← Calcul pondéré d'un type de mention
│   ├── 📄 calculer_probabilites_admission.py ← Probabilités par type de bac
│   ├── 📄 calculer_repartition_mentions.py   ← Répartition complète des mentions
│   ├── 📄 construire_resultats.py         ← Agrège toutes les données pour l'affichage
│   └── 📄 mettre_a_jour_listes.py        ← Mise à jour dynamique des listes
│
├── 📁 static/                              ← Ressources statiques
│   ├── 📄 fr-esr-parcoursup.csv           ← Données officielles Parcoursup (data.gouv.fr)
│   ├── 📄 prompt.txt                       ← Prompt système du chatbot IA
│   ├── 🖼️  amine.png, jarod.png, mouheb.png, logo.png
│   └── 📁 css/
│       └── 📄 style.css
│
├── 📁 templates/                           ← Pages HTML (Jinja2)
│   ├── 📄 ACCUEIL.html                    ← Page d'accueil
│   ├── 📄 CHATBOT.html                    ← Interface du chatbot IA
│   ├── 📄 PROGRAMME.html                  ← Présentation des spécialités
│   ├── 📄 index.html                       ← Simulateur Parcoursup
│   ├── 📄 CONSEIL.html                    ← Conseils et témoignages
│   └── 📄 HISTOIRE.html                   ← Histoire du projet
│
└── 📁 tests/                              ← Tests unitaires (1 fichier = 1 fonction)
    ├── 📄 test_definir_listes.py
    ├── 📄 test_filtrer_donnees.py
    ├── 📄 test_calculer_mention.py
    ├── 📄 test_calculer_probabilites_admission.py
    ├── 📄 test_calculer_repartition_mentions.py
    ├── 📄 test_construire_resultats.py
    └── 📄 test_mettre_a_jour_listes.py
```

---

## 🤖 Le chatbot IA

Le chatbot est propulsé par l'**API Mistral AI** avec le modèle `mistral-small-latest`.

Il est spécialisé grâce à un **prompt système** qui lui donne le rôle d'un conseiller d'orientation scolaire. Il est capable de :

- 🎯 Recommander des combinaisons de spécialités selon le profil de l'élève
- 📈 Expliquer les liens entre spécialités et filières post-bac
- ⚠️ Mettre en garde contre les risques de mauvais choix
- 💬 Adapter son discours au niveau scolaire perçu

**Architecture de la requête :**

```python
response = client.chat.complete(
    model="mistral-small-latest",
    messages=[
        {"role": "system", "content": prompt},   # Prompt d'orientation
        {"role": "user",   "content": question}  # Question de l'élève
    ]
)
```

---

## 📊 Le simulateur Parcoursup

Le simulateur utilise le fichier de données officiel **`fr-esr-parcoursup.csv`** publié sur [data.gouv.fr](https://www.data.gouv.fr), traité avec **Pandas**.

### Fonctionnalités

- Filtrage dynamique par **région**, **ville**, **filière** et **établissement**
- Calcul des **probabilités d'admission** par type de bac (général, technologique, professionnel)
- Calcul de la **répartition des mentions** des admis
- Mise à jour des listes déroulantes en temps réel (requêtes AJAX)

### Fonctions principales

| Fonction | Fichier | Description |
|---|---|---|
| `definir_listes(df)` | `fonctions/definir_listes.py` | Génère les 5 listes de filtres depuis le DataFrame |
| `filtrer_donnees(...)` | `fonctions/filtrer_donnees.py` | Applique les filtres successifs sur le DataFrame |
| `calculer_probabilites_admission(df)` | `fonctions/calculer_probabilites_admission.py` | Calcule les % d'admission par type de bac |
| `calculer_mention(colonne, data)` | `fonctions/calculer_mention.py` | Calcul pondéré d'un type de mention |
| `calculer_repartition_mentions(df)` | `fonctions/calculer_repartition_mentions.py` | Répartition complète des 4 mentions |
| `construire_resultats(...)` | `fonctions/construire_resultats.py` | Agrège toutes les données pour l'affichage |
| `mettre_a_jour_listes(...)` | `fonctions/mettre_a_jour_listes.py` | Met à jour les listes déroulantes (AJAX) |

---

## 🧪 Lancer les tests

Les tests unitaires couvrent les fonctions critiques du simulateur Parcoursup.

```bash
# Depuis la racine du projet, avec l'environnement virtuel activé :
pytest test/

# Pour un affichage détaillé :
pytest test/ -v

# Pour un rapport de couverture :
pytest test/ --cov=sources
```

### Tests disponibles

| Fichier de test | Fonction testée | Ce qui est vérifié |
|------|-------------------|--------------------|
| `test_definir_listes.py` | `definir_listes()` | Type tuple, 5 listes triées, non vides |
| `test_filtrer_donnees.py` | `filtrer_donnees()` | Cohérence des filtres, cas vide (région inexistante) |
| `test_calculer_mention.py` | `calculer_mention()` | Type float, bornes 0–100 |
| `test_calculer_probabilites_admission.py` | `calculer_probabilites_admission()` | Gestion DataFrame vide, type float, bornes 0–100 |
| `test_calculer_repartition_mentions.py` | `calculer_repartition_mentions()` | Valeurs attendues pour un établissement de référence |
| `test_construire_resultats.py` | `construire_resultats()` | Structure du dictionnaire de retour |
| `test_mettre_a_jour_listes.py` | `mettre_a_jour_listes()` | Listes triées, valeurs attendues, cas vide |

---

## 👥 Équipe

<div align="center">

<table>
  <tr>
    <td align="center" width="280">
      <img src="static/amine.png" width="80" style="border-radius:50%"/><br><br>
      <img src="https://img.shields.io/badge/Amine-Créateur-3b82f6?style=for-the-badge&logoColor=white"/>
      <br><br>
      <b>Développeur principal</b><br><br>
      <img src="https://img.shields.io/badge/Flask-Back--end-000000?style=flat-square&logo=flask"/>
      <img src="https://img.shields.io/badge/Mistral-IA-FF7000?style=flat-square"/>
      <img src="https://img.shields.io/badge/Pandas-Données-150458?style=flat-square&logo=pandas"/>
      <img src="https://img.shields.io/badge/Tailwind-Design-06B6D4?style=flat-square&logo=tailwindcss"/>
      <br><br>
      <i>Conception de l'architecture, développement full-stack, intégration API Mistral, simulateur Parcoursup</i>
    </td>
    <td align="center" width="280">
      <img src="static/anas.png" width="80" style="border-radius:50%"/><br><br>
      <img src="https://img.shields.io/badge/Jarod-Architecture-8b5cf6?style=for-the-badge&logoColor=white"/>
      <br><br>
      <b>Restructuration & Qualité</b><br><br>
      <img src="https://img.shields.io/badge/Refactorisation-Code-8b5cf6?style=flat-square"/>
      <img src="https://img.shields.io/badge/Modules-Organisation-6d28d9?style=flat-square"/>
      <br><br>
      <i>Refactorisation du code, organisation des modules, mise en conformité avec les normes du concours</i>
    </td>
    <td align="center" width="280">
      <img src="static/gibaud.jpeg" width="80" style="border-radius:50%"/><br><br>
      <img src="https://img.shields.io/badge/Mouheb-Tests-3b82f6?style=for-the-badge&logoColor=white"/>
      <br><br>
      <b>Tests & Documentation</b><br><br>
      <img src="https://img.shields.io/badge/Pytest-Tests-0A9EDC?style=flat-square&logo=pytest"/>
      <img src="https://img.shields.io/badge/Documentation-Qualité-22c55e?style=flat-square"/>
      <br><br>
      <i>Fonctions de test unitaires, vérification de la reproductibilité, documentation technique</i>
    </td>
  </tr>
</table>

<br>

![Lycée Newton](https://img.shields.io/badge/Lycée_Isaac_Newton-Clichy-3b82f6?style=for-the-badge&logo=google-maps&logoColor=white)
![Terminale NSI](https://img.shields.io/badge/Terminale-NSI-8b5cf6?style=for-the-badge&logoColor=white)
![Trophées NSI](https://img.shields.io/badge/Trophées_NSI-2026-6d28d9?style=for-the-badge&logoColor=white)

</div>

---

<div align="center">

**Cap Spé** — Projet réalisé dans le cadre des *Trophées NSI 2026*

Lycée Isaac Newton · Clichy · Académie de Versailles

[![Trophées NSI](https://img.shields.io/badge/Troph%C3%A9es_NSI-2026-6D28D9?style=for-the-badge)](https://trophees-nsi.fr)

</div>
