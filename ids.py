from packages import utils
import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        print("ben")
    elif len(sys.argv) > 1 and sys.argv[1] == "prepare":
        data = utils.JsonManager.PrepareData()
        utils.JsonManager.Write("/var/ids/db.json", data)

if __name__ == "__main__":
    main()