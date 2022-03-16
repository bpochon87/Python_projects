"""
- Import sqlite3 module
- dB requires two fields: an ID INTEGER PRIMARY KEY AUTOINCREMENT, and a field
  with the DT 'str' [TEXT]
- Read from supplied list of names, determine only '.txt' files.
- Add '.txt' files to dB.
- Print '.txt' files to console in legible manner.
"""

# Import module to work with.
import sqlite3


def createTable():
    # Connect to dB.
    connect = sqlite3.connect('assignment.db')
    # 'With' opens the dB. "While we have this open, do..."
    with connect:
        # Move cursor off connection
        cursor = connect.cursor()
        # We can execute an SQL statement with 'execute()'.
        cursor.execute("CREATE TABLE IF NOT EXISTS text_files(\
                        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                        col_desc TEXT)")
        # The above code is committed to dB.
        connect.commit()
    # Close dB.
    connect.close()


def postFiles():
    # List to iterate through to find text files.
    fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', \
                'World.txt', 'data.pdf', 'myPhoto.jpg')
    # Reopen dB to import textFiles into.
    connect = sqlite3.connect('assignment.db')
    for file in fileList:
        # This variable will help find files with .txt suffix.
        txt = '.txt'
        if txt in file:
            print(file)
            # Post files into database.
            with connect:
                cursor = connect.cursor()
                cursor.execute("INSERT INTO text_files(col_desc) VALUES (?)", \
                                (file,))
                connect.commit()
    connect.close()
        

if __name__ == "__main__":
    createTable()
    postFiles()


