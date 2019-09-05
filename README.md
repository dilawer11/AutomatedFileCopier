# AutomatedFileCopier
Automatically Copies any file added to one directory into another

Requirements:
Python3 
Watchdogs

Usage $python3 moveFiles.py init "Folder/To/Copy/From" "Folder/To/Copy/To"

"Folder/To/Copy/From" and "Folder/To/Copy/To" must be relative paths 

Example Usage $python3 moveFiles.py init Desktop/FromFolder Desktop/ToFolder

Process runs in background to kill it run the following command

$ ps ax | grep moveFiles.py

and then kill the PID e.g

$ kill 0000

replace 0000 with PID from the earlier command
