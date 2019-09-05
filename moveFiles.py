from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys
import os
import json
import time
path_to_track = ""
path_to_copy = ""
selfName = sys.argv[0]
class MyHandler(FileSystemEventHandler):
    def on_modified(self,event):
        for filename in os.listdir(path_to_track):
            src = path_to_track + "/" + filename
            new_destination = path_to_copy + "/" + filename
            os.rename(src, new_destination)
def startBackground(folder_to_track, destination_folder):
    global path_to_track
    global path_to_copy
    path_to_track = os.path.join(os.getcwd(), folder_to_track)
    path_to_copy = os.path.join(os.getcwd(), destination_folder)
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path_to_track, recursive=True)
    observer.start()
    observer.join()
def init(folder_to_track, destination_folder):
    os.system("chmod +x " + selfName)
    os.system("nohup python3 " + selfName + " start " + folder_to_track + " " + destination_folder + " &")
if(sys.argv[1] == "init"):
    init(sys.argv[2],sys.argv[3])
elif(sys.argv[1] == "start"):
    startBackground(sys.argv[2],sys.argv[3])
else:
    print("Invalid Arguments")
