import git
from os import linesep
from datetime import datetime
import json

def autosave(path):
    ''' Add changed files, commit, push '''
    cmd = git.cmd.Git(path)
    if cmd.status(porcelain=True):
        cmd.add(".")
        cmd.commit(message=f"{datetime.now()} autosave")
        cmd.push()
        print(f"[ OK    ] {datetime.now()} saved {path} ")


if __name__ == "__main__":
    with open("autosave.json") as jsonFile:
        data = json.load(jsonFile)
    try:
        for path in data["folders"]:
            autosave(path)
    except Exception as e:
        print(f"[ ERROR ] {datetime.now()} something went wrong.")
        print("{e}")
