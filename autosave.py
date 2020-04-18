import git
from os import linesep 
from datetime import datetime

cmd = git.cmd.Git()
if "" != cmd.status(porcelain=True):
    cmd.add(".")
    cmd.commit(message=f"{datetime.now()} autosave")
    cmd.push()