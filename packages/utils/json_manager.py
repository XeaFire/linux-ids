import json
import sys
from .file_manager import FileManager
from .folder_manager import FolderManager

class JsonManager:
    def Parse(pathfile : str):
        if FileManager.GetInfo(pathfile,"size") == 0:
            return
        try:
            with open(pathfile) as f:
                d = json.load(f)
                return d
        except json.decoder.JSONDecodeError:
            print("il manque un json là ohhhh")
            sys.exit(1)


    def Write(pathfile : str, data):
        with open(pathfile, 'w') as f:
            json.dump(data, f)

    def EditKey(pathfile : str, key : str, data):
        pass
 
    def DeleteKey(pathfile : str, key : str, data):
        pass

    def PrepareData():
        data = JsonManager.Parse("ids-config.json")
        filepath = data.get("filepath", "")
        folderpaths = data.get("folderpath", [])
        result = []
        for file in filepath:
            entry = FileManager.GetAllInfos(file)
            result[folder] = entry
        for folder in folderpaths:
            entry = FolderManager.GetAllInfos(folder)
            result[folder] = entry

        return result


    def UpdateDB(data):
        JsonManager.Write("/var/ids/db.json", data)

    def VerifyJson(pathfolder : str, data):
        old_data = JsonManager.Parse(pathfolder)
        if (old_data == data):
            return True
        else:
            return False