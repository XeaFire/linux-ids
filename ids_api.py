from packages import utils
from flask import Flask, abort, jsonify
import json

# on crée un ptit objet Flask, nécessaire pour ajouter des routes
app = Flask(__name__)
app.secret_key = b'SECRET_KEY'

# utilisation d'un décorateur Python avec @ pour donc décorer une fonction
# c'est l'ajout de ce décorateur qui permet d'ajouter une route
# c'est dans la doc de Flask, nous on obéit :D
@app.route('/reports', methods=['GET'])
def get_users():
    utils.JsonManager.Parse("/var/ids/db.json")

    # Flask fournit une méthode jsonify() qui permet de retourner des objets Python sous format JSON de façon adaptée
    return jsonify(users)

@app.route('/report/<user_id>', methods=['GET'])
def get_user(user_id=None):
    file = open("data/users.json")
    users = json.load(file)
    file.close()

    if user_id in users:
        results = jsonify(users[user_id])
        return results
    else:
        # la ptite 404 clean quand on demande une ressource qui n'existe pas
        abort(404)

    return jsonify(users)

@app.route('/check>', methods=['POST'])
def Check():
    data = utils.JsonManager.PrepareData()
        
    old_data = utils.JsonManager.Parse("/var/ids/db.json")
    if old_data == data :
        print("State : Ok")
    else:
        print("State : Divergent")
        print("Les fichiers / dossiers modifiés sont : " + ", ".join(utils.JsonManager.CompareData(old_data,data)))
    utils.JsonManager.Write("/var/ids/db.json", data)
    utils.BonusManager.SendDiscordAlert("Les fichiers / dossiers modifiés sont : " + ", ".join(utils.JsonManager.CompareData(old_data,data)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
