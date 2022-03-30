#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import Python-based modules.
import os
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox

# Import modules made by me.
import phonebook_main
import phonebook_gui


def centerWindow(self, w, h): # Pass in Tkinter Frame(master) reference and the w and h.
    # Get user's screen width and height.
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # Calculate X and Y coordinates to center App on user's screen.
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry("{}x{}+{}+{}".format(w, h, x, y))
    return centerGeo


# Catch if user clicks on windows upper right X. Ensure their decision.
def ask_quit(self):
    # Messagebox is just that: message box to the user.
    # First string, "Exit program", is title of messagebox. Second string is message to user.
    if messagebox.askokcancel("Exit Program", "Okay to exit application?"):
        # This closes app.
        self.master.destroy()
        # This takes all widgets and fully deletes them from memory.
        os._exit(0)


###################################################################################################


def create_db(self):
    connect = sqlite3.connect("phonebook.db")
    with connect:
        cursor = connect.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );")
        # Commit changes to dB and then close dB connection.
        connect.commit()
    connect.close()
    first_run(self)

def first_run(self):
    data = ("Brady", "Pochon", "Brady Pochon", "308-280-0070", "bpochon@gmail.com")
    connect = sqlite3.connect("phonebook.db")
    with connect:
        cursor = connect.cursor()
        cursor,count = count_records(cursor)
        if count < 1:
            cursor.execute("""INSERT INTO tbl_phonebook (col_fname, col_lname, col_fullname,"""
                           """col_phone, col_email) VALUES (?,?,?,?,?)""", (data))
            connect.commit()
    connect.close()


def count_records(cursor):
    count = ""
    cursor.execute("""SELECT COUNT (*) FROM tbl_phonebook""")
    count = cursor.fetchone()[0]
    return cursor,count

#Select item in ListBox
def onSelect(self, event):
    # Calling event is th self.lstList1 widget.
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    connect = sqlite3.connect("phonebook.db")
    with connect:
        cursor = connect.cursor()
        cursor.execute("""SELECT col_fname, col_lname, col_phone, col_email FROM tbl_phonebook """
                       """WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # Returns a tuple where it's sliced into four parts using data[] during the iteration.
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # Normalize the data to keep it consistent in the dB.
    var_fname = var_fname.strip() # Removes blank spaces before and after user entry.
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname, var_lname)) # Combine normalized names into a full name.
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    # User must fill out all Entry boxes.
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0):
        connect = sqlite3.connect("phonebook.db")
        with connect:
            cursor = connect.cursor()
            # Check dB for existence of fullname. If found, user alerted and request disregarded.
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname """
                           """= '{}'""".format(var_fullname)) # ,(var_fullname)
            count = cursor.fetchone() [0]
            chkName = count
            # If chkName is zero, there's no existence of full name and new data can be added.
            if chkName == 0:
                print("chkName: {}".format(chkName))
                cursor.execute("""INSERT INTO tbl_phonebook(col_fname, col_lname, col_fullname, """
                               """col_phone, col_email) VALUES (?,?,?,?,?)""",(var_fname, var_lname,
                                                                               var_fullname, var_phone,
                                                                               var_email))
                self.lstList1.insert(END, var_fullname) # Update listbox with new full name.
                onClear(self) # Call function to clear all of the textboxes.
            else:
                messagebox.showerror("Name Error","'{}' already exists in database. Please choose "
                                     "a different name.".format(var_fullname))
                onClear(self) # Call function to clear all Entry boxes.
        connect.commit()
        connect.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure data is present in all four fields.")

def onDelete(self):
    # Listbox's selected value.
    var_select = self.lstList1.get(self.lstList1.curselection())
    connect = sqlite3.connect("phonebook.db")
    with connect:
        cursor = connect.cursor()
        # Check count to ensure this isn't last record in dB. Last record cannot be deleted else
        # there will be an error.
        cursor.execute("""SELECT COUNT (*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with """
                                            """\n({})\n will be permanently deleted.""".format(var_select))
            if confirm:
                connect = sqlite3.connect("phonebook.db")
                with connect:
                    cursor = connect.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) # Call function to clear all Entry boxes and selected index of listbox
##                  onRefresh(self) # Update listbox with changes.
                connect.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database "
                                           "and cannot be deleted at this time.\n\nPlease add another "
                                           "record before deleting ({}).".format(var_select, var_select))
    connect.close()

def onDeleted(self):
    # Clear text in these Entry boxes.
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
##      onRefresh(self) # Update listbox with changes.
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass


def onClear(self):
    # Clear text in these Entry boxes.
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)


def onRefresh(self):
    # Populate listbox according to dB.
    self.lstList1.delete(0,END)
    connect = sqlite3.connect("phonebook.db")
    with connect:
        cursor = connect.cursor()
        cursor.execute("""SELECT COUNT (*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_phonebook""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i += 1
    connect.close()


def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] # Index of list selection.
        var_value = self.lstList1.get(var_select) # List selection's text value.
    except:
        messagebox.showinfo("Missing Selection","No name was selected from the list box.\nCancelling"
                            "the Update request.")
        return
    # User will only be allowed to update changes for phone and email.
    # For name change, use will need to delete entire record and start again.
    var_phone = self.txt_phone.get().strip() # Normalize data to maintain dB integrity.
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0): # Ensure data is present.
        connect = sqlite3.connect("phonebook.db")
        with connect:
            
            cursor = connect.cursor()
            # Count records to see if user's changes already exist (no changes to update).
            cursor.execute("""SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone """
                           """= '{}'""".format(var_phone))
            count = cursor.fetchone()[0]
            print(count)
            cursor.execute("""SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email """
                           """= '{}'""".format(var_email))
            count2 = cursor.fetchone()[0]
            print(count2)
            if count == 0 or count2 == 0: # If proposed changes don't already exist, proceed.
                response = messagebox.askokcancel("Update Request","The following changes ({}) and ({}) "
                                              "will be implemented for ({}).\n\nProceed with the "
                                              "update request?".format(var_phone, var_email, var_value))
                print(response)
                if response:
                    with connect:
                        cursor = connect.cursor()
                        cursor.execute("""UPDATE tbl_phonebook SET col_phone = '{0}', col_email = '{1}' WHERE """
                                       """col_fullname = '{2}'""".format(var_phone, var_email, var_value))
                        onClear(self)
                        connect.commit()
                else:
                    messagebox.showinfo("Cancel Request","No changes were made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No Changes Detected","Both ({}) and ({}) exist already in this database "
                                    "for this name. Your update request has been cancelled.".format(var_phone,
                                                                                                    var_email))
            onClear(self)
        connect.close()
    else:
        messagebox.showerror("Missing Information","Please select a name from the list and then you may edit "
                             "phone or email information.")
    onClear(self)

if __name__ == "__main__":
    pass                       
