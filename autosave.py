import git
from os import linesep 
from datetime import datetime

cmd = git.cmd.Git()
res = cmd.status(porcelain=True)
filesToBeSaved = len(res.split(linesep)) > 0
if filesToBeSaved:
    cmd.add(".")
    cmd.commit(message=f"{datetime.now()} autosave")
    cmd.push()