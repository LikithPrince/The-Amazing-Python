
import csv

csv_file=open("csvdata.csv",mode='w', newline='')
csv_data=csv.writer(csv_file)

csv_data.writerow(['Slno',"Name","address"])
csv_data.writerows([['1',"likith","Mandya"],['2',"Nithin","Hassan"],['3',"Girish","Bangalore"],["4","Vyshak",'Kerala'],["5",'Ashwini',"Bangalore"]])
csv_file.close()
