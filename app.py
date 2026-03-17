#Projet : CapSpé
#Auteurs : Amine, Jarod, Mouheb

import os
import pandas as pd
from flask import Flask, render_template, request, jsonify
from mistralai import Mistral
from dotenv import load_dotenv
from fonctions.construire_resultats import construire_resultats
from fonctions.mettre_a_jour_listes import mettre_a_jour_listes

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv('API_KEY')
MODEL_NAME = "mistral-small-latest"
client = Mistral(api_key=API_KEY)

# Chemin relatif et portable (fonctionne sur Windows, macOS et Linux)
dataframe = pd.read_csv(
    os.sep.join(["static", "fr-esr-parcoursup.csv"]),
    sep=";", encoding='cp1252', low_memory=False
)


@app.route('/')
def home():
    stats = {
        'nombre_premieres': 9,
        'nombre_profs': 5,
        'nombre_terminales': 10,
    }
    return render_template("ACCUEIL.html", stats=stats)


@app.route('/vide')
def vide():
    return render_template("VIDE.html")


@app.route('/programme')
def programme():
    return render_template("PROGRAMME.html")


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/conseil')
def conseil():
    return render_template("CONSEIL.html")


@app.route('/histoire')
def histoire():
    return render_template("HISTOIRE.html")


@app.route("/compute", methods=["POST"])
def compute():
    cles = ["lieu", "choix_dep", "choix_ville", "choix_fil", "choix_postbac", 'choix_etablissement']
    parametres = {k: request.form.get(k) for k in cles}
    parametres['dataframe'] = dataframe
    result = construire_resultats(parametres)
    return jsonify(result)


@app.route("/change_liste", methods=["POST"])
def change_liste():
    keys = ["lieu", "choix_dep", "choix_ville", "choix_fil", "choix_postbac", 'choix_etablissement']
    parametres = {k: request.form.get(k) for k in keys}
    parametres['dataframe'] = dataframe
    result = mettre_a_jour_listes(parametres)
    return jsonify(result)


@app.route('/chatbot')
def chatbot():
    return render_template("CHATBOT.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_prompt = data.get("prompt", "").strip()

    if not user_prompt:
        return jsonify({"response": "Je n'ai pas bien compris votre question."})

    try:
        prompt_path = os.sep.join(["static", "prompt.txt"])
        with open(prompt_path, 'r', encoding='utf-8') as f:
            prompt = f.read()

        response = client.chat.complete(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        if response.choices:
            answer = response.choices[0].message.content
            return jsonify({"response": answer})
        return jsonify({"response": "⚠️ L'IA n'a pas renvoyé de réponse."})

    except Exception as e:
        print(f"ERREUR MISTRAL: {e}")
        return jsonify({"response": f"Désolé, j'ai rencontré une erreur technique : {str(e)}"})


if __name__ == "__main__":
    app.run(debug=True)
