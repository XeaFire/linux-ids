from hashlib import sha512, sha256, md5
import os
class FileManager:
    def GetHash(filepath : str, hash = "sha256") -> str:
        f = open(filepath, "r")
        r = ""
        if (hash == "sha512"):
            r = sha512(f.read().encode('utf-8')).hexdigest()
        elif (hash == "md5"):
            r = md5(f.read().encode('utf-8')).hexdigest()
        else:
            r = sha256(f.read().encode('utf-8')).hexdigest()
        return r
    
    def GetInfo(filepath : str, info = str) -> str:
        r = ""
        if (info == "size"):
            r = os.path.getsize(filepath)
        elif (info == "cdate"):
            r = os.path.getctime(filepath)
        elif (info == "mdate"):
            r = os.path.getmtime(filepath)
        return r