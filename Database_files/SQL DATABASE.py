
import sqlite3



connection_obj = sqlite3.connect('DBeaver.db')



cursor_obj = connection_obj.cursor()



# cursor_obj.execute("DROP TABLE STUDENT")



table = """ CREATE TABLE STUDENT (NAME VARCHAR(255), CLASS VARCHAR(255),SECTION VARCHAR(255));"""

cursor_obj.execute(table)

cursor_obj.execute('''INSERT INTO STUDENT VALUES ('Raju', '7th', 'A')''')

cursor_obj.execute('''INSERT INTO STUDENT VALUES ('Shyam', '8th', 'B')''')

cursor_obj.execute('''INSERT INTO STUDENT VALUES ('Baburao', '9th', 'C')''')



print("Data Inserted in the table: ")



data=cursor_obj.execute('''SELECT * FROM STUDENT''')

for row in data:

    print(row)



connection_obj.commit()

connection_obj.close()    