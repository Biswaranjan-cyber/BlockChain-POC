import MySQLdb as sql
import hashing as hash

theChain = []

def connection(id,passw,dataBase):
    """connects to the local dbms with data provided"""
    db = sql.connect("localhost",str(id),str(passw),str(dataBase))
    cursor = db.cursor()
    return db,cursor

def exits(db):
    """function for closing the access to database"""
    db.close
    print("Closing!!!!")

def lookAll(thatCursor,table):
    """prints the entire data in the table being looked for"""

    try:
        line = "SELECT * FROM %s"%(str(table))
        thatCursor.execute(line)
        print("The entirety of the %r table in database" % table)
        results = thatCursor.fetchall()
        for info in results:
            print(info)

    except Exception as e:
        print("Error at LookAll:",e)

def blockEncoder(thatCursor,table):
    """this will encode the data into blockchain"""
    try:
        columns = fields(thatCursor,table)
        line = "SELECT * FROM %s" % (str(table))
        thatCursor.execute(line)
        results = thatCursor.fetchall()
        data = []
        for info in results:
            strips = ""
            for i in info:
                if info.index(i) == 0:
                    strips = str( columns [info.index(i)] ) + ":" + str(i)
                    #strips = strips + ","
                else:
                    lines = str( columns [info.index(i)] ) + ":" + str(i)
                    strips = strips + "," +lines
            data.append(strips)

        theChain = hash.addingBlocks(data)
    except Exception as e:
        print("Error at BlockEncoder:",e)

def fields(themCursor,table):
    """finds the name of fields in the table"""
    sql = "desc %s"% (str(table))
    themCursor.execute(sql)
    results = themCursor.fetchall()
    fieldValues = []
    for info in results:
        #the field names are the first elements
        #and we get first one in each row of the description
        fieldValues.append(info[0])
    return fieldValues

def helper():
    """prints the help for all functions"""
    print("Help of all function in order")
    help(connection)
    help(lookAll)
    help(fields)
    help(blockEncoder)
    help(exits)
