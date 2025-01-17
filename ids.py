from packages import utils
import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        Check()
    elif len(sys.argv) > 1 and sys.argv[1] == "build":
        pass
    


def Check():
    data = utils.JsonManager.PrepareData()
        
    old_data = utils.JsonManager.Parse("/var/ids/db.json")
    if old_data == data :
        print("State : Ok")
    else:
        print("State : Divergent")
        print("Les fichiers / dossiers modifiés sont : " + utils.JsonManager.CompareData(data,old_data))
    utils.JsonManager.Write("/var/ids/db.json", data)


if __name__ == "__main__":
    main()