import os
import sys
from os import listdir
from os.path import isfile, join

from time import gmtime, strftime

event = sys.argv[2]

parent_dir = sys.argv[1]
file_name = sys.argv[3]
flashback_dir = ".flash/"
this_flashback_dir= parent_dir+flashback_dir
if not os.path.exists(this_flashback_dir):
        os.makedirs(this_flashback_dir)

now = strftime("%Y-%m-%d-%H:%M:%S", gmtime())

def dir_to_files(dir):
    return  [ f for f in listdir(dir) if isfile(join(dir,f)) ]

def file_to_backups(f,flashback_dir):
    print f
    return [ff for ff in dir_to_files(flashback_dir) if f in ff].sort()

print str(dir_to_files(this_flashback_dir))
print str(file_to_backups(file_name,this_flashback_dir))
    
