from os.path import walk
import os
import sys

genesis_dir = sys.argv[1] 
flashback_dir = ".flash/"

def myvisit(a, dir, files):
    print dir
    if dir[-5:]!= ".flash": 
        parent_dir = dir+"/"
        this_flashback_dir= parent_dir+flashback_dir

        if not os.path.exists(this_flashback_dir):
            os.makedirs(this_flashback_dir)
        for f in files:
            if os.path.isfile(f):
                os.system("ln " + parent_dir+f + " " + this_flashback_dir + f) 


def pleaseclean(a,dir,files):
    if dir.split("/")[-1] == ".flash":
        os.system("rm -r "+dir) 

walk(genesis_dir, myvisit, None)
#walk(genesis_dir, pleaseclean, None)
