import Threads
import Testing

print("Welcome to Blockchain encoding demo file")
print("Enter the details of the DBMS you want to edit"),
print("and it's credential data")

db,cursor = Testing.login()          #although it is not logical to do so much returns
table_name = Testing.tableToOperate()     #it is done so that programs can be as modular as possible

try:

    print("Select any one of following operations")
    print("1.See all data in table of current database.")
    print("2.Encode all data into hashes and form blockchain database.")
    print("3.Read the extended help file attached with program.")
    print("4.Exit the program")
    while True:
        choice = input(">>>")
        try:
            Testing.switching(choice,db,cursor,table_name)
        except Exception as e:
            print("Enter a valid Choice(1-4)")
            print(e)

except Exception as e:
    print("Error:",e)

