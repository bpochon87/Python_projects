#!/usr/bin/python
""" Recommended way when it's an executable Python script.
    Documentation 2.2.2 Executable Python Scripts:
    In a Unix-like operating system, the program loader
    takes the presence of these two characters as an
    indication that the file is a script, and tries to
    execute that script using the interpreter specified
    by the rest of the first line in the file.
"""
#-*- coding: utf-8 -*-
""" #-*- coding: utf-8 -*-
    This sets charset if it's present on first two lines of file. This is syntax
    to declare encoding of a Python file source file. Discussed in PEP 0263,
    Defining Python Source Code Encodings
"""


# Python version:   3.9.1
#
# Author:           Brady Logan Pochon
#
# Purpose:          Python course step #317.
#
# Tested OS:        Code was written and tested on Windows 10.


import tkinter as tk
from tkinter import *

# This library allows dialog modal to browse computer files.
from tkinter import filedialog

# This script contains the functions.
import fileTransferAssignment_func
# This script contains the GUI.
import fileTransferAssignment_gui

# The frame will be passed onto the window.
class ParentWindow(Frame):
    # Once class is defined, it's referred to as 'self'.
    # master references Frame from Tkinter.
    def __init__(self, root, *args, **kwargs):
        Frame.__init__(self, root, *args, **kwargs)

        # Root frame configuration.
        self.master = root
        self.master.configure(bg='skyblue')
        self.master.title("Check For New Files")
        self.master.geometry('532x180')
        self.master.resizable(False, False)
        arg = self.master
      


        # Located in fileTransferAssignment_gui.
        fileTransferAssignment_gui.load_gui(self)







if __name__ == '__main__':
    # This syntax creates window.
    root = tk.Tk()
    # Class ParentWindow being attached to root (the window) and called App.
    App = ParentWindow(root)
    # This must be included for program to run.
    root.mainloop()
