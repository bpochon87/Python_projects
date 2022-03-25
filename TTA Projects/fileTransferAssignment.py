# Set folder that has created/modified text files as source.
# Set folder that is destination file as destination.
# Iterate through files in source folder and check modification time.
# If modification time <24hrs, move file to destination folder.

# Will allow files to be moved
import shutil

from datetime import date

# This will allow us to convert from epoch to local time.
import time

# Import os because we need os.listdir() which gets the list of all files and directories
# in the specified directory.
# We will also use os.path.getmtime() which will give us the modification time of the file
# in epoch form where we'll have to convert for ability to check if <24 hours old.
import os

# Source folder where we'll check files and their modification times.
source = 'D:/Users/bpoch/Desktop/FolderA/'

# Destination folder where <24 hour modified files will be transferred to.
destination = 'D:/Users/bpoch/Desktop/FolderB/'


"""
1) For this function, need to iterate through each file in source folder.
2) For each file, check modification time.
3) For each modification time, convert to <24 hour.
4) If <24 hr mod time, move to destination folder.
5) If >24 hr mod time, leave alone.
"""
def moveFile():
    # Setting variable for .txt suffix only files.
    txtSuffix = '.txt'
    # Creating list of files from source file path.
    files = os.listdir(source)
    # Iterating through list to find .txt files only. Will go through all of them.
    for file in files:
        # If .txt is found, call on convertTime() and pass in that file.
        if txtSuffix in file:
            fileModificationDate = convertTime(file)
            # From datetime module bringing in today's date.
            todayDate = date.today()
            if todayDate == fileModificationDate:
                shutil.move(source + file, destination)
          
        

def convertTime(file):
    # Letting this function know path.
    source = 'D:/Users/bpoch/Desktop/FolderA/'
    # Returning mod time in epoch.
    modTimeEpoch = os.path.getmtime('D:/Users/bpoch/Desktop/FolderA/' + file)
    # Convert seconds since epoch to readable timestamp. We're only concerned about the
    # past 24 hours.
    return time.strftime('%Y-%m-%d', time.localtime(modTimeEpoch))

    
    









if __name__ == "__main__":
    moveFile()
    
