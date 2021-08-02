import sqlite3

def executeCommand(command):
    conn = sqlite3.connect("my_grades.db") # Creates or Connects to a DB
    c = conn.cursor() # Create Cursor
    c.execute(command)
    conn.commit() # Commit the changes
    conn.close() # Close the connection

def executeFetch(command):
    conn = sqlite3.connect("my_grades.db") # Creates or Connects to a DB
    c = conn.cursor() # Create Cursor
    c.execute(command)
    fetchedData = c.fetchall()
    conn.commit() # Commit the changes
    conn.close() # Close the connection

    return fetchedData

def executeInsert(command, subject, credit_score, grade):
    conn = sqlite3.connect("my_grades.db") # Creates or Connects to a DB
    c = conn.cursor() # Create Cursor
    c.execute(command, (subject, credit_score, grade))
    conn.commit() # Commit the changes
    conn.close() # Close the connection

def createTablesDB():
    # First Year
    firstfs = ''' CREATE TABLE IF NOT EXISTS first_firstSem(
        subject TEXT,
        credit_score FLOAT,
        grade FLOAT) '''
    executeCommand(firstfs)

    firstss = ''' CREATE TABLE IF NOT EXISTS first_secondSem(
        subject TEXT,
        credit_score FLOAT,
        grade FLOAT) '''
    executeCommand(firstss)

    # Second Year
    secondfs = ''' CREATE TABLE IF NOT EXISTS second_firstSem(
        subject TEXT,
        credit_score FLOAT,
        grade FLOAT) '''
    executeCommand(secondfs)

    secondss = ''' CREATE TABLE IF NOT EXISTS second_secondSem(
        subject TEXT,
        credit_score FLOAT,
        grade FLOAT) '''
    executeCommand(secondss)

    # Third Year
    thirdfs = ''' CREATE TABLE IF NOT EXISTS third_firstSem(
        subject TEXT,
        credit_score FLOAT,
        grade FLOAT) '''
    executeCommand(thirdfs)

    thirdss = ''' CREATE TABLE IF NOT EXISTS third_secondSem(
        subject TEXT,
        credit_score FLOAT,
        grade FLOAT) '''
    executeCommand(thirdss)

    # Fourth Year
    fourthfs = ''' CREATE TABLE IF NOT EXISTS fourth_firstSem(
        subject TEXT,
        credit_score FLOAT,
        grade FLOAT) '''
    executeCommand(fourthfs)

    fourthss = ''' CREATE TABLE IF NOT EXISTS fourth_secondSem(
        subject TEXT,
        credit_score FLOAT,
        grade FLOAT) '''
    executeCommand(fourthss)

def getDataFromDB():
    # Needed for presentation to the screen of all the data
    # 1
    selectFFS = "SELECT subject, credit_score, grade FROM first_firstSem ORDER BY grade"
    ffirstSem = executeFetch(selectFFS)

    selectFSS = "SELECT subject, credit_score, grade FROM first_secondSem ORDER BY grade"
    fsecondSem = executeFetch(selectFSS)

    # 2
    selectSFS = "SELECT subject, credit_score, grade FROM second_firstSem ORDER BY grade"
    sfirstSem = executeFetch(selectSFS)

    selectSSS = "SELECT subject, credit_score, grade FROM second_secondSem ORDER BY grade"
    ssecondSem = executeFetch(selectSSS)

    # 3
    selectTFS = "SELECT subject, credit_score, grade FROM third_firstSem ORDER BY grade"
    tfirstSem = executeFetch(selectTFS)

    selectTSS = "SELECT subject, credit_score, grade FROM third_secondSem ORDER BY grade"
    tsecondSem = executeFetch(selectTSS)

    # 4
    selectFRFS = "SELECT subject, credit_score, grade FROM fourth_firstSem ORDER BY grade"
    frfirstSem = executeFetch(selectFRFS)

    selectFRSS = "SELECT subject, credit_score, grade FROM fourth_secondSem ORDER BY grade"
    frsecondSem = executeFetch(selectFRSS)

    return ffirstSem, fsecondSem, sfirstSem, ssecondSem, tfirstSem, tsecondSem, frfirstSem, frsecondSem

def insertDB(items, table):
    for item in items:
        item = item.text() # Comverts into text the value of item
        original_length = len(item) # Gets the length of item
        compressed = item.replace('\t', '') # It deletes the \t: TAB compressing the data
        length = original_length - 7 # Gets the numbers at the end 
        trimmed = item[length:original_length] 

        subject = compressed[0:original_length-8]
        grade = trimmed[4:7]
        credit_score = trimmed[0:3]

        executeInsert("INSERT INTO {}(subject, credit_score, grade) VALUES(?, ?, ?)".format(table), subject, credit_score, grade)