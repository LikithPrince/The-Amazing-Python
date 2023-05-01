
import sqlite3


############## CONNECTION TO DATABASE #############
############## CREATING DATABASE FILE #############

connect_=sqlite3.connect("books.db")
cursor_=connect_.cursor()



############## CREATING PARENT TABLE ################


PARENT_TABLE=('''create table Teacher 
(
T_no number(2) primary key,
Name varchar2(20) not null,
M_no number(10) unique not null

) 
''')

# cursor_.execute(PARENT_TABLE)


################ INSERTING VALUES INTO TABLE ###################

insert_values=(" insert into Teacher values (?,?,?)")

data_parent_Table =[ 

('01','Girish','7767755755'),

('02','Nithin','9966809755'),

('03','Girish Kumar','8899778644'),

('04','Abhishek','8050809404') 

]

cursor_.executemany(insert_values,data_parent_Table)



############## CREATING CHILD TABLE ################

CREATE_TABLE=('''create table Enno 
(
Sl_no number(2) primary key,
Name varchar2(20) not null,
Age number(2) not null,
Address varchar2(30) not null,
M_no number(10) unique not null,
Email varchar2(30) unique not null,
T_no number(2),
constraint fk foreign key(T_no) references Teacher(T_no)
) 
''')

# cursor_.execute(CREATE_TABLE)


################ INSERTING VALUES INTO TABLE ###################


insert_data=(" insert into Enno values (?,?,?,?,?,?,?)")

data =[ 

('01','Girish','27','KR Puram','7767755755','girish@gmail.com','1'),

('02','Nithin','26','Hassan','9966809755','nithin@gmail.com','3'),

('03','Girish Kumar','35','Kerala','8899778644','girishkumar@gmail.com','3'),

('04','Abhishek','31','Mumbai','8050809404','abhishek@gmail.com','4') 

]

cursor_.executemany(insert_data,data)



#################### FOR DELETE TABLE ######################## 



# cursor_.execute('drop table Enno')




###################### TO FETCH DATA FROM TABLE ###################

# cursor_.execute("select * from Enno")
# out=cursor_.fetchall()
# print(out)

##################### SAVING DATA ######################

connect_.commit()
connect_.close()