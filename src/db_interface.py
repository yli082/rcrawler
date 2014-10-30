import sqlite3

#if not already done, creates the database tableUCR Rants
def create_db_table():
    try:
	#opens the database
        db = sqlite3.connect("results.db")
	#creates a cursor to interact with the db
        cursor = db.cursor()
	#creates the table
        cursor.execute("CREATE TABLE searchIndex(Id INT, Key TEXT NOT NULL, Links TEXT NOT NULL)")
	#commits the changes 
        db.commit()
	#closes the database
        db.close()
    except:
        return

#clears the database
def clear_db():
    #opens the database
    db = sqlite3.connect("results.db")
    #creates a cursor to interact with the db
    cursor = db.cursor()
    #deletes the contents of searchIndex
    cursor.execute("DELETE FROM searchIndex")
    #wipes the memory
    cursor.execute("vacuum")
    #commits the changes
    db.commit()
    #closes the database
    db.close()

#updates the database
def update_db(index):
    #print "updating db"
	
    #if not already done, creates the table
    create_db_table()
	
    #opens the database
    db = sqlite3.connect("results.db")
    #creates a cursor to interact with the db
    cursor = db.cursor()
    #clears the table
    clear_db()
	
    #initializes the id count
    id_db = 0
	
    #for each key in the index dictionary 
    for i in index:
	#add a new row with the corresponding values
        cursor.execute("INSERT INTO searchIndex VALUES(?, ?, ?)", 
            (id_db, i, str(index[i])))
	#increment the id count
        id_db += 1
		
    #commits the changes
    db.commit()
    #closes the database
    db.close()
