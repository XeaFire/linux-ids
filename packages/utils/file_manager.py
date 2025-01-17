from hashlib import sha512, sha256, md5
import json
import os
from pwd import getpwuid

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
    
    def GetInfo(filepath : str, info = str) -> float:
        r = ""
        if (info == "size"):
            r = os.path.getsize(filepath)
        elif (info == "cdate"):
            r = os.path.getctime(filepath)
        elif (info == "mdate"):
            r = os.path.getmtime(filepath)
        return r
    
    def GetOwner(filename):
        return getpwuid(os.stat(filename).st_uid).pw_name

    def GetAllInfos(filepath : str, entrytype):
        if entrytype == "file":
            s = FileManager.GetInfo(filepath, "size")
            c = FileManager.GetInfo(filepath, "cdate")
            m = FileManager.GetInfo(filepath, "mdate")
            infos = {
                "size" : s,
                "cdate" : c,
                "mdate" : m,
                "SHA512" : FileManager.GetHash(filepath, "sha512"),
                "SHA256" : FileManager.GetHash(filepath, "sha256"),
                "MD5" : FileManager.GetHash(filepath, "md5"),
                "Owner" : FileManager.GetOwner(filepath) 
            }
        return infos