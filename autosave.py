import git
from os import linesep 
from datetime import datetime

cmd = git.cmd.Git()
res = cmd.status(porcelain=True)
filesToBeSaved = "" != res and len(res.split(linesep)) > 0
if filesToBeSaved:
    print(len(res.split(linesep)))
    print(res)
    print("something changed")
    # cmd.add(".")
    # cmd.commit(message=f"{datetime.now()} autosave")
    # cmd.push()