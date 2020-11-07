#Deletes or trashes the ALTTPR folder and all it's contents (seeds/ROMs, screenshots, etc)

#Possilble Future Changes:
#Change it (or give an option) to only delete *.sfc files in said folder
#Show how many files were deleted/trashed

#Imported modules
import os
import shutil
from send2trash import send2trash

#Intro message
print("""The Legend of Zelda: A Link to the Past Randomizer (ALTTPR) Folder Cleaner v.021
""")

#Input prompt
trash = input('[D]elete or [T]rash the folder?: ')

#Trash
if trash == ("t") or trash == ("T"):
    send2trash("/Users/obeast/Downloads/ROMs/SNES/ALTTPR")
    os.mkdir("/Users/obeast/Downloads/ROMs/SNES/ALTTPR")
    print("ALTTPR folder trashed!")

#Delete
elif trash == ("d") or trash == ("D"):
    shutil.rmtree("/Users/obeast/Downloads/ROMs/SNES/ALTTPR")
    os.mkdir("/Users/obeast/Downloads/ROMs/SNES/ALTTPR")
    print("ALTTPR folder deleted!")

#Invalid input message
else:
    print("""Invalid Input. 
Exiting Program.""")