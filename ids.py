from packages import utils

def main():
    ben = input("plop")
    print(utils.HashManager.GetHash(ben, "sha256"))
    

if __name__ == "__main__":
    main()