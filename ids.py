from packages import utils

def main():
    ben = input("plop")
    print(utils.FileManager.GetHash(ben, "sha256"))
    data = utils.FileManager.GetAllInfos(ben)
    utils.JsonManager.Write("/var/ids/db.json", data)
    print(utils.JsonManager.Parse("/var/ids/db.json"))
    print(utils.JsonManager.VerifyJson("/var/ids/db.json"))
    

if __name__ == "__main__":
    main()