from hashlib import sha512, sha256, md5
import json
import os
from pwd import getpwuid

class FolderManager:
    def GetHash(folderpath: str, hash="sha256") -> str:
        combined_hash = sha256() if hash == "sha256" else sha512() if hash == "sha512" else md5()
        for root, dirs, files in os.walk(folderpath):
            for filename in files:
                filepath = os.path.join(root, filename)
                with open(filepath, "r", errors='ignore') as f:
                    combined_hash.update(f.read().encode('utf-8'))
        return combined_hash.hexdigest()

    def GetInfo(folderpath: str, info=str) -> float:
        r = ""
        if info == "size":
            r = sum(os.path.getsize(os.path.join(root, f)) for root, _, files in os.walk(folderpath) for f in files)
        elif info == "cdate":
            r = min(os.path.getctime(os.path.join(root, f)) for root, _, files in os.walk(folderpath) for f in files)
        elif info == "mdate":
            r = max(os.path.getmtime(os.path.join(root, f)) for root, _, files in os.walk(folderpath) for f in files)
        return r

    def GetOwner(folderpath):
        return getpwuid(os.stat(folderpath).st_uid).pw_name

    def GetAllInfos(folderpath: str):
        s = FolderManager.GetInfo(folderpath, "size")
        c = FolderManager.GetInfo(folderpath, "cdate")
        m = FolderManager.GetInfo(folderpath, "mdate")
        infos = {
            "size": s,
            "cdate": c,
            "mdate": m,
            "SHA512": FolderManager.GetHash(folderpath, "sha512"),
            "SHA256": FolderManager.GetHash(folderpath, "sha256"),
            "MD5": FolderManager.GetHash(folderpath, "md5"),
            "Owner": FolderManager.GetOwner(folderpath)
        }
        return infos
