from packages import utils

def main():
    ben = input("plop")
    print(utils.FileManager.GetHash(ben, "sha256"))
    data = utils.FileManager.GetAllInfos(ben)
    utils.JsonManager.Write("./test.json", data)
    

if __name__ == "__main__":
    main()