#!/bin/zsh
# crete similar script and add it to corntab (linux/osx)
# 1.) chmod +x /pathtoyourscript/autosave.zsh
# 2.) corntab -e
# 3.) * * * * * /pathtoyourscript/autosave.zsh
cd /Users/dbalogh/dev/python/autosave # containing folder of autosave.py
/Users/dbalogh/dev/python/envs/autosave/bin/python autosave.py #path to your python3 executable
