# Create file if not exists.
# Append to file HTML code.
# Save file.
# Open file in browser.

import webbrowser
from tkinter import *
import tkinter as tk
from tkinter import messagebox


#### FUNCTIONS ####

#def htmlScript():
#    file = open("script.html", 'w')
#    file.write("<html><body><h1>Stay tuned for our amazing summer sale!</h1></body></html>")
#    file.close()
#    webbrowser.open_new('D:/Users/bpoch/Desktop/Python projects/script.html')

def load_gui(self):
    # Creating Label (tkinter class) and their position using grid().
    self.lbl_enterText = Label(self.root, text="Enter text for HTML body: ", bg='skyblue')
    self.lbl_enterText.grid(row=0, column=0, padx=(5), pady=(5), sticky=N+E+S+W)

    # Text box.
    self.txt_enterText = Text(self.root, height=5, width=50)
    self.txt_enterText.grid(row=0, column=1, pady=(10))

    # Button for submission of new HTML body text.
    self.btn_submit = Button(self.root, text="Submit", command=lambda: getTextInput(self))
    self.btn_submit.grid(row=1, column=1, sticky=E)


# This will take text input from window and create new file with it added in as HTML.
# A web browser will then open.
def getTextInput(self):
    text = self.txt_enterText.get('1.0', END)
    file = open("script.html", 'w')
    file.write("<html><body><h1>" + text + "</h1></body></html>")
    file.close()
    webbrowser.open_new('script.html')
    
    









#### GUI #####
    
## Main configurations
    
# The frame will be passed onto the window.
class ParentWindow(Frame):
    def __init__(self, root, *args, **kwargs):
        Frame.__init__(self, root, *args, **kwargs)

        # Define master Frame configuration.
        self.root = root
        self.root.minsize(580, 150)
        self.root.maxsize(580, 150)
        self.root.configure(bg='skyblue')
        self.root.title("Update HTML")
        self.root.protocol("WM_DELETE_WINDOW")
        arg = self.root
        self.root.grid()

        root = tk.Tk()

        
        
        # Call to load_gui func to load widgets.
        load_gui(self)
        






    
    
if __name__ == "__main__":
    # Creating new window.
    root = tk.Tk()
    # Attaching class ParentWindow to root (the window)
    App = ParentWindow(root)
    # Loop to continue tkinter window showing.
    root.mainloop()
