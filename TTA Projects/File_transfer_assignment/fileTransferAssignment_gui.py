#!/usr/bin/python
#-*- coding: utf-8 -*-


import tkinter as tk
from tkinter import *

# This library allows dialog modal to browse computer files.
from tkinter import filedialog

# This script contains the functions.
import fileTransferAssignment_func
# This script contains the class ParentWindow.
import fileTransferAssignment_main


def load_gui(self):
    # Labels and their positioning on grid.
    self.lbl_selectFilesFrom = tk.Label(self.master, text="Select files less than a day old from:", bg="skyblue")
    self.lbl_selectFilesFrom.grid(row=0, column=1, columnspan=3, pady=(5), sticky=S+W+E)

    self.lbl_sendFilesTo = tk.Label(self.master, text="Move files less than a day old to:", bg="skyblue")
    self.lbl_sendFilesTo.grid(row=4, column=1, columnspan=3, pady=(5), sticky=S+W+E)

    # Entry boxes, their StringVar(), and their positioning on grid.
    # StringVar() is set up to change with changing of selected directory.
    self.browseButton1Text = tk.StringVar(self.master)
    self.browseButton2Text = tk.StringVar(self.master)
    
    self.txt_selectFilesFrom = tk.Entry(self.master, text="", width=75, textvariable = self.browseButton1Text)
    self.txt_selectFilesFrom.grid(row=2, column=1, rowspan=1, columnspan=3, padx=(5), pady=(5), sticky=W)

    self.txt_sendFilesTo = tk.Entry(self.master, text="", width=75, textvariable = self.browseButton2Text)
    self.txt_sendFilesTo.grid(row=5, column=1, rowspan=1, columnspan=4, padx=(5), pady=(5), sticky=W)

    # Buttons and their positioning on grid.
    self.btn_browse1 = tk.Button(self.master, text="Browse...", command=lambda: fileTransferAssignment_func.filesFromDirectory(self))
    self.btn_browse1.grid(row=2, column=0, padx=(5), pady=(5))

    self.btn_browse2 = tk.Button(self.master, text="Browse...", command=lambda: fileTransferAssignment_func.filesToDirectory(self))
    self.btn_browse2.grid(row=5, column=0, padx=(5), pady=(5))

    self.btn_submit = tk.Button(self.master, text="Submit", command=lambda: fileTransferAssignment_func.transferFiles(self))
    self.btn_submit.grid(row=6, column=3, padx=(5), pady=(5), sticky=E)
    
    










if __name__ == "__main__":
    pass
