import json

class JsonManager:
    def Parse(pathfile : str):
        with open(pathfile) as f:
            d = json.load(f)
            return d

    def Write(pathfile : str, data):
        with open(pathfile, 'w') as f:
            json.dump(data, f)

    def EditKey(pathfile : str, key : str, data):
        pass
 
    def DeleteKey(pathfile : str, key : str, data):
        pass

    def UpdateDB(data):
        pass

    def VerifyJson(pathfolder : str, data):
        old_data = JsonManager.Parse(pathfolder)
        if (old_data == data):
            return True
        else:
            return False