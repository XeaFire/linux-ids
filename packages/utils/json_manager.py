import json

class JsonManager:
    def Parse(pathfile : str):
        pass

    def Write(pathfile : str, data):
        with open(pathfile, 'w') as f:
            json.dump(data, f)