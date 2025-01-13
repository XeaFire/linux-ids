import json

class JsonManager:
    def Parse(pathfile : str):
        with open('strings.json') as f:
            d = json.load(f)
            return d

    def Write(pathfile : str, data):
        with open(pathfile, 'w') as f:
            json.dump(data, f)

    def UpdateDB():
        pass