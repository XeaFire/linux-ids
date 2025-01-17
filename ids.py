from packages import utils

def main():
    # ben = input("")
    # print(utils.FileManager.GetHash(ben, "sha256"))
    # data = utils.FileManager.GetAllInfos(ben)
    # print(utils.JsonManager.VerifyJson("/var/ids/db.json", data))
    # utils.JsonManager.Write("/var/ids/db.json", data)
    # print(utils.JsonManager.Parse("/var/ids/db.json"))
    
    data = utils.JsonManager.PrepareData()
    utils.JsonManager.Write("/var/ids/db.json", data)

if __name__ == "__main__":
    main()