from packages import utils

def main():
    ben = input("plop")
    print(utils.FileManager.GetHash(ben, "sha256"))
    print(utils.FileManager.GetInfo(ben, "size"))
    print(utils.FileManager.GetInfo(ben, "cdate"))
    print(utils.FileManager.GetInfo(ben, "mdate"))
    

if __name__ == "__main__":
    main()