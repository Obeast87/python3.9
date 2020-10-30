print("The Legend of Zelda: A Link to the Past Randomizer (ALTTPR) folder cleaner v.01")
print("")

#Imported modules
import os
import shutil

#Deletes the ALTTPR folder and all it's contents (seeds/ROMs, screenshots, etc)
#Will have the script move them to trash as an option
shutil.rmtree("/Users/obeast/Downloads/ROMs/SNES/ALTTPR")

#Creates new empty ALTTPR folder to replace deleted/trashed folder
#I want to have it delete just the .sfc files and/or files that start with "alttp", but this will do
os.mkdir("/Users/obeast/Downloads/ROMs/SNES/ALTTPR")

#Success message
#Will add "X number of files/seeds deleted or moved to trash" message
#Will add failure/errored out message
print("ALTTPR folder cleaned!")
print("Now, go waste another hour getting lost in a dungeon while in Go Mode!")
