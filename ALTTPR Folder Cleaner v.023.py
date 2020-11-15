#Deletes or trashes the ALTTPR folder and all it's contents (seeds/ROMs, screenshots, etc)

#Possilble Future Changes:
#Change it (or give an option) to only delete *.sfc files in said folder
#Show how many files were deleted/trashed

#Changes in .022/.023
#Simplified folder location part of script to hopefully save space
#Added "are you sure?" input for deleting the folder
#Added Simpsons reference/meme because why not

#Imported modules
import os
import shutil
from send2trash import send2trash

#Folder Location
folder = ("/Users/obeast/Downloads/ROMS/SNES/ALTTPR")

#Intro message
print("""The Legend of Zelda: A Link to the Past Randomizer (ALTTPR) Folder Cleaner v.023
""")

#Beginning input prompt
trash = input('[D]elete or [T]rash the folder, or press [A]ny key to exit?: ')

#Trash
if trash == ("t") or trash == ("T"):
    send2trash(folder)
    os.mkdir(folder)
    print("ALTTPR folder trashed")

#Prompt for delete
elif trash == ("d") or trash == ("D"):
    delete = input("Are you sure you want to fully delete this folder?: ")
    if delete == ("y") or delete == ("Y"):
        shutil.rmtree(folder)
        os.mkdir(folder)
        print("ALTTPR folder deleted")
    else:
        print("ALTTPR folder not deleted")

#Any key
elif trash == ("a") or trash == ("A"):
    print("""Where's the "any" key?""")

#Invalid input message
else:
    print("Invalid Input")

print("")
