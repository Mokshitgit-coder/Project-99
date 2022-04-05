import os
import shutil

folderName=input("Enter source of the folder")
destination=input("Enter the destination")

folderName=folderName+"/"
destination=destination+"/"

list_of_files=os.listdir(folderName)

for file in list_of_files:
    shutil.copy((folderName+file),destination)