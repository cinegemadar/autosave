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


if __name__ == "__main__":
    with open("autosave.json") as jsonFile:
        data = json.load(jsonFile)
    try:
        for path in data["folders"]:
            autosave(path)
    except:
        print("fatal: not a git repository (or any of the parent directories)")
