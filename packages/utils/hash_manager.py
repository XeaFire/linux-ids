from hashlib import sha512, sha256, md5

class HashManager:
    def GetHash(filepath : str, hash = "sha256") -> str:
        f = open(filepath, "r")
        r = ""
        if (hash == "sha512"):
            r = sha512(filepath.encode('utf-8')).hexdigest()
        elif (hash == "md5"):
            r = md5(filepath.encode('utf-8')).hexdigest()
        else:
            r = sha256(filepath.encode('utf-8')).hexdigest()
        return r

