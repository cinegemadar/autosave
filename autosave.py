import git
from os import linesep 
from datetime import datetime

        

def autosave():
    cmd = git.cmd.Git()
    if cmd.status(porcelain=True):
        cmd.add(".")
        cmd.commit(message=f"{datetime.now()} autosave")
        cmd.push()
        
if __name__ == "__main__":
    try:
        autosave()
    except:
        print("fatal: not a git repository (or any of the parent directories)")