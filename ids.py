from packages import utils
import sys
import os

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        Check()
    elif len(sys.argv) > 1 and sys.argv[1] == "build":
        Build()
    

def Build():
    if os.geteuid() != 0:
        raise PermissionError("Execute le build avec sudo sinon tu n'auras pas de Low Taper Fade héhéhéhé")
    if not os.path.isfile('/var/ids/db.json'):
        utils.JsonManager.Write("/var/ids/db.json", "{}")
        

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


if __name__ == "__main__":
    main()