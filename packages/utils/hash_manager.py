class HashManager:
    def GetHashFromFile(path : str) -> str:
        f = open(path, "r")
        print(f.read())

    def GetHashFromFolder(path : str) -> str:
        pass