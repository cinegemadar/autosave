import git
from os import linesep 

cmd = git.cmd.Git()
res = cmd.status(porcelain=True)
filesToBeSaved = len(res.split(linesep)) > 0
if filesToBeSaved:
    cmd.add(".")
    cmd.commit(message="autosave")
    cmd.push()