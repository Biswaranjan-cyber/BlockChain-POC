import Threads
import webbrowser
from sys import exit

#these codes perform work of paramount importance
#donot change anything here
def login():
     try:
            id = input("\t                Id>>>")
            passw = input("\t          Password>>>")
            dataBase = input("\t     Database Name>>>")
            return Threads.connection(id, passw, dataBase)

     except Exception as e:
            print("Error during Login:\n",e)

def tableToOperate():      #opens the table on which work is to be done
    print("Enter the name of table in the database "),
    tableName = input(">>>")
    return tableName


def openTxt():  # opens the help file
    webbrowser.open("help.txt")


def die(db):  # closes the python program
    try:
        Threads.close(db)
    except:
        print("Closing program")
        exit(0)



def switching(choice,db,cursor,table_name):
    options = {
        '1': Threads.lookAll(cursor,table_name) ,
        '2': Threads.blockEncoder(cursor,table_name) ,
        '3': openTxt(),
        '4': die(db)
    }

    func = options[choice]
    func()