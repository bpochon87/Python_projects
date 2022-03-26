#!/usr/bin/python
#-*- coding: utf-8 -*-


# Will allow files to be moved
import shutil

# This library allows dialog modal to browse computer files.
from tkinter import filedialog

from datetime import date, datetime, timedelta

# Import os because we need os.listdir() which gets the list of all files and directories
# in the specified directory.
import os

import fileTransferAssignment_main
import fileTransferAssignment_gui

# Source folder where we'll check files and their modification times.
source = self.browseButton1Text.get()

# Destination folder where <24 hour modified files will be transferred to.
destination = self.browseButton2Text.get()


def transferFiles():
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
            todayDate = datetime.now()
            twentyFourHoursAgo = todayDate - timedelta(hours=24)
            if fileModificationDate > twentyFourHoursAgo:
                shutil.move(source + file, destination)
          
        

def convertTime(file):
    # Letting this function know path.
    source = self.browseButton1Text.get()
    # Returning mod time in epoch.
    modTimeEpoch = os.path.getmtime(source + file)
    return datetime.fromtimestamp(modTimeEpoch)


# When browse button clicked, bring up filedialog window for both buttons.

def filesFromDirectory(self):
    self.directoryPath = filedialog.askdirectory(initialdir = 'C:\\', title="Choose File")
    self.browseButton1Text.set(self.directoryPath)

def filesToDirectory(self):
    self.directoryPath = filedialog.askdirectory(initialdir = 'C:\\', title="Choose File")
    self.browseButton2Text.set(self.directoryPath)
    









if __name__ == "__main__":
    pass
    
