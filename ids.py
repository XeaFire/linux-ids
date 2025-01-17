from packages import utils
import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        data = utils.JsonManager.PrepareData()
        utils.JsonManager.Write("/var/ids/db.json", data)
        old_data = utils.JsonManager.Parse("/var/ids/db.json")
        if old_data == data :
            print("State : Ok")
        else:
            print("State : Divergent")
    elif len(sys.argv) > 1 and sys.argv[1] == "build":
        pass

if __name__ == "__main__":
    main()