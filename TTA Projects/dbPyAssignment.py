import sqlite3

def createTable():
    with sqlite3.connect(':memory:') as connection:
        c = connection.cursor()
        peopleValues = (('Jean-Baptiste Zorg', 'Human', '122'), ('Korben Dallas', 'Meat Popsicle', '100'),
                        ('Ak\'not', 'Mangalore', '-5'))
        c.execute("CREATE TABLE IF NOT EXISTS Roster(Name TEXT, Species TEXT, IQ INT)")
        c.execute("INSERT INTO Roster(Name, Species, IQ) VALUES(?,?,?)", peopleValues)
        c.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas'")
        c.execute("SELECT * FROM Roster WHERE Species = Human")
    connection.close()


    

if __name__ == '__main__':
    createTable()
