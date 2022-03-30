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
# Purpose:          Mock phonebook app demonstrating OOP and Tkinter GUI module,
#                   using Tkinter Parent and Child relationships.
#
# Tested OS:        Code was written and tested on Windows 10.

# Import tkinter module and its widgets
from tkinter import *
import tkinter as tk
from tkinter import messagebox



# Import modules containing rest of code for program to function correctly.
import phonebook_gui
import phonebook_func


# Frame is the Tkinter class that our own class will inherit from.
class ParentWindow(Frame):
    # Once class is defined, it's referred to as 'self'.
    # Master references Frame from Tkinter.
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define master Frame configuration.
        self.master = master
        self.master.minsize(500,300)   # (Height, Width) in pixels. Locked size.
        self.master.maxsize(500,300)
        # centerWindow method will center app on user's screen.
        phonebook_func.centerWindow(self,500,300)
        self.master.title("Brady's Tkinter Phonebook")
        self.master.configure(bg="#F0F0F0")
        # Protocol method is a Tkinter built-in that catches if user clicks
        # the upper corner "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Load GUI widgets from separate module. This is to keep code compartmentalized.
        phonebook_gui.load_gui(self)



if __name__ == "__main__":
    # This syntax creates window.
    root = tk.Tk()
    # Class (ParentWindow) is being attached to root (the window) and called App.
    App = ParentWindow(root)
    # This must be included for program to run.
    root.mainloop()
    
