import git
from os import linesep 
from datetime import datetime

cmd = git.cmd.Git()
res = cmd.status(porcelain=True)
filesToBeSaved = len(res.split(linesep)) > 0
if filesToBeSaved:
    cmd.add(".")
    # timestamp =  datetime.fromtimestamp(datetime.timestamp(datetime.now()))
    timestamp =  datetime.now()
    cmd.commit(message=f"{timestamp} autosave")
    cmd.push()